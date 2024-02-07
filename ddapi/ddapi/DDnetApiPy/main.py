import aiohttp
from aiohttp import ClientSession
from typing import Union
from json import JSONDecoder
from aiohttp.typedefs import DEFAULT_JSON_DECODER
from ..errors import ExceptConnection
from ..dataclass import DDPlayer
from ..misc import username_encode


class DDnetApi:
    def __init__(self,
                 session: ClientSession = None,
                 on_raise: bool = True,
                 json_loads: JSONDecoder = DEFAULT_JSON_DECODER):
        self.session = session
        self.on_raise = on_raise
        self.json_loads = json_loads
        self.url = "https://ddstats.qwik.space/player/json?player={0}"

    @property
    def closed(self):
        return self.session.closed is None or self.session.closed

    async def _ch_start(self) -> None:
        if self.session is None:
            self.session = aiohttp.ClientSession()

    async def _send(self, url: str) -> Union[dict, None]:
        await self._ch_start()
        try:
            async with self.session.get(url) as req:
                if req.status == 200:
                    usr = await req.text()
                    if usr == '{}' or usr is None:
                        return
                    del usr
                    return await req.json(loads=self.json_loads)
                return
        except Exception as ex:
            if self.on_raise:
                raise ExceptConnection(f"This hosting may not be available at the moment: {ex}")
            return

    async def close(self) -> None:
        return await self.session.close()

    async def player(self, player: str) -> Union[DDPlayer, None]:
        dat = await self._send(f"https://ddnet.org/players/?json2={username_encode(player)}")
        if dat is None:
            return
        return DDPlayer(**dat)

    async def dict_player(self, player: str) -> Union[dict, None]:
        dat = await self._send(f"https://ddnet.org/players/?json2={username_encode(player)}")
        if dat is None:
            return
        return dat

    async def master(self) -> Union[dict, None]:
        return await self._send("https://master1.ddnet.org/ddnet/15/servers.json")
