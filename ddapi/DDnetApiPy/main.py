import aiohttp
import orjson
from aiohttp import ClientSession
from ..dataclass import DDPlayer
from ..misc import username_encode


class DDnetApi:
    def __init__(self, session: ClientSession = None):
        self.session = session
        self.url = "https://ddstats.qwik.space/player/json?player={0}"

    @property
    def closed(self):
        return self.session.closed is None or self.session.closed

    async def _ch_start(self) -> None:
        if self.session is None:
            self.session = aiohttp.ClientSession()

    async def _send(self, url: str) -> dict | None:
        await self._ch_start()
        async with self.session.get(url) as req:
            if req.status == 200:
                usr = await req.text()
                if usr == '{}' or usr is None:
                    return
                del usr
                return await req.json(loads=orjson.loads)
            return

    async def close(self) -> None:
        return await self.session.close()

    async def player(self, player: str) -> DDPlayer | None:
        dat = await self._send(f"https://ddnet.org/players/?json2={username_encode(player)}")
        if dat is None:
            return
        return DDPlayer(**dat)

    async def dict_player(self, player: str) -> dict | None:
        dat = await self._send(f"https://ddnet.org/players/?json2={username_encode(player)}")
        if dat is None:
            return
        return dat

    async def master(self) -> dict | None:
        return await self._send("https://master1.ddnet.org/ddnet/15/servers.json")
