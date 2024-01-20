import aiohttp
import orjson
from aiohttp import ClientSession
from ..dataclass import Player
from ..misc import username_encode
from ..errors import ExceptConnection


class QwikAPI:
    def __init__(self, session: ClientSession = None):
        self.session = session
        self.url = "https://ddstats.qwik.space/player/json?player={0}"

    @property
    def closed(self):
        return self.session.closed is None or self.session.closed

    async def _ch_start(self) -> None:
        if self.session is None:
            self.session = aiohttp.ClientSession()

    async def _send(self, player: str) -> dict | None:
        await self._ch_start()
        try:
            async with self.session.get(self.url.format(username_encode(player))) as req:
                if req.status == 200:
                    usr = await req.text()
                    if usr == '{}' or usr is None:
                        return
                    del usr
                    return await req.json(loads=orjson.loads)
                return
        except Exception as ex:
            raise ExceptConnection(f"This hosting may not be available at the moment: {ex}")

    async def player(self, nickname) -> Player | None:
        dat = await self._send(nickname)
        if not dat:
            return
        return Player(**dat)

    async def close(self) -> None:
        await self.session.close()
