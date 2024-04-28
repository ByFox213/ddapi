import re
from typing import Union
from json import JSONDecoder
from urllib.parse import quote

import aiohttp
from aiohttp import ClientSession, ClientConnectorError
from aiohttp.typedefs import DEFAULT_JSON_DECODER
from .dataclass import DDPlayer, Master, Player, Query, STPlayer, STServers, STServer, STClients, STClans, STGameTypes, \
    STMaps, STVersions, STMastersStats, STBans

reg_server = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


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

    async def query(self, player: str) -> Union[Query, None]:
        dat = await self._send(f"https://ddnet.org/players/?query={quote(player)}")
        if dat is None:
            return
        dat = {'data': dat}
        return Query(**dat)

    async def master(self) -> Union[Master, None]:
        dat = await self._send("https://master1.ddnet.org/ddnet/15/servers.json")
        if dat is None:
            return
        return Master(**dat)


class QwikAPI(API):
    async def player(self, nickname) -> Union[Player, None]:
        dat = await self._send(f"https://ddstats.qwik.space/player/json?player={quote(nickname)}")
        if not dat:
            return
        return Player(**dat)


class StatusAPI(API):
    async def players(self) -> Union[STClients, None]:
        dat = await self._send("https://api.status.tw/player/list")
        if not dat:
            return
        dat = {"players": dat}
        return STClients(**dat)

    async def player(self, nickname) -> Union[STPlayer, None]:
        dat = await self._send(f"https://api.status.tw/player/details/{quote(nickname)}")
        if not dat:
            return
        return STPlayer(**dat)

    async def server(self, ip: str, port: int) -> Union[STServer, None]:
        if not re.search(reg_server, ip):
            return
        dat = await self._send(f"https://api.status.tw/server/details/{ip}/{port}")
        if not dat:
            return
        return STServer(**dat)

    async def servers(self) -> Union[STServers, None]:
        dat = await self._send("https://api.status.tw/server/list/")
        if not dat:
            return
        dat = {"servers": dat}
        return STServers(**dat)

    async def clans(self) -> Union[STClans, None]:
        dat = await self._send("https://api.status.tw/clan/list")
        if not dat:
            return
        dat = {"clans": dat}
        return STClans(**dat)

    async def gametype(self) -> Union[STGameTypes, None]:
        dat = await self._send("https://api.status.tw/gametype/list")
        if not dat:
            return
        dat = {"gametypes": dat}
        return STGameTypes(**dat)

    async def maps(self) -> Union[STMaps, None]:
        dat = await self._send("https://api.status.tw/map/list")
        if not dat:
            return
        dat = {"maps": dat}
        return STMaps(**dat)

    async def bans(self) -> Union[STBans, None]:
        dat = await self._send("https://api.status.tw/map/list")
        if not dat:
            return
        dat = {"bans": dat}
        return STBans(**dat)

    async def versions(self) -> Union[STVersions, None]:
        dat = await self._send("https://api.status.tw/map/list")
        if not dat:
            return
        dat = {"versions": dat}
        return STVersions(**dat)

    async def masters_stats(self) -> Union[STMastersStats, None]:
        dat = await self._send("https://api.status.tw/map/list")
        if not dat:
            return
        dat = {"masters": dat}
        return STMastersStats(**dat)
