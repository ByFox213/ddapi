from typing import Union
from json import JSONDecoder
from urllib.parse import quote

import aiohttp
from aiohttp import ClientSession, ClientConnectorError
from aiohttp.typedefs import DEFAULT_JSON_DECODER
from .dataclass import DDPlayer, Master, Player


class API:
    def __init__(self,
                 session: ClientSession = None,
                 ex: bool = False,
                 json_loads: JSONDecoder = DEFAULT_JSON_DECODER):
        self.session = session
        self.json_loads = json_loads
        self.ex = ex
        self.url = "https://ddstats.qwik.space/player/json?player={0}"

    def __del__(self):
        self.session = None

    @property
    def closed(self):
        return self.session.closed is None or self.session.closed

    async def _send(self, url: str) -> Union[dict, None]:
        if self.session is None:
            self.session = aiohttp.ClientSession()
        try:
            async with self.session.get(url) as req:
                if req.status == 200:
                    usr = await req.text()
                    if usr == '{}' or usr is None:
                        return
                    del usr
                    return await req.json(loads=self.json_loads)
        except ClientConnectorError:
            if self.ex:
                raise ClientConnectorError
            return

    async def close(self) -> None:
        return await self.session.close()


class DDnetApi(API):
    async def player(self, player: str) -> Union[DDPlayer, None]:
        dat = await self._send(f"https://ddnet.org/players/?json2={quote(player)}")
        if dat is None:
            return
        return DDPlayer(**dat)

    async def master(self) -> Union[Master, None]:
        dat = await self._send("https://master1.ddnet.org/ddnet/15/servers.json")
        if dat is None:
            return
        return Master(**dat)


class DDraceAPI(API):
    async def player(self, nickname) -> Union[Player, None]:
        dat = await self._send(f"https://ddstats.qwik.space/player/json?player={quote(nickname)}")
        if not dat:
            return
        return Player(**dat)
