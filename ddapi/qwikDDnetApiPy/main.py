import aiohttp
import orjson
from aiohttp import ClientSession

from ddapi.dataclass import Player

sum_to_encoding = {"␣": "%20", "!": "%21", "\"": "%22", "#": "%23",
                   "$": "%24", "%": "%25", "&": "%26", "\'": "%27",
                   "(": "%28", ")": "%29", "*": "%2A", "+": "%2B",
                   ",": "%2C", "/": "%2F", ":": "%3A", ";": "%3B",
                   "=": "%3D", "?": "%3F", "@": "%40", "[": "%5B",
                   "]": "%5D", "-": "%2D", ".": "%2E", "<": "%3C",
                   ">": "%3E", "\\": "%5C", "^": "%5E", "_": "%5F",
                   "`": "%60", "{": "%7B", "|": "%7C", "}": "%7D",
                   "~": "%7E"}


def username_encode(username: str) -> str:
    """Decodes the line so that http gives out information about the player.
    :param username:
        :type: str
    :return:
        :type: str
    """
    result: str = ""
    for i in username:
        add: str = sum_to_encoding.get(i)
        if add is not None:
            result += add
        else:
            result += i
    return result


class DDraceAPI:
    def __init__(self, session: ClientSession = None):
        self.session = session
        self.url = "https://ddstats.qwik.space/player/json?player={0}"

    async def _ch_start(self) -> None:
        if self.session is None:
            self.session = aiohttp.ClientSession()

    async def _send(self, nick: str) -> dict | None:
        await self._ch_start()
        async with self.session.get(self.url.format(username_encode(nick))) as req:
            if req.status == 200:
                usr = await req.text()
                if usr == '{}' or usr is None:
                    return
                del usr
                return await req.json(loads=orjson.loads)
            return

    async def player(self, nickname) -> Player | None:
        dat = await self._send(nickname)
        if not dat:
            return
        return Player(**dat)

    async def close(self) -> None:
        await self.session.close()
