from enum import StrEnum
from typing import Union
from urllib.parse import quote

from .api import API
from .scheme import DDPlayer, Master, Query, DMap, DDStatus, Player, MasterTw, ServerTwOne, ChartEnum, Charts, \
    QueryMapper, QueryMap, ReleasesMaps

__all__ = (
    "DDnetApi",
    "DDstats",
    "Status"
)


class MasterEnum(StrEnum):
    master1 = "master1"
    master2 = "master2"
    master3 = "master3"
    master4 = "master4"


class DDnetApi(API):
    def __init__(self):
        super().__init__()
        self.domain = "ddnet.org"

    @staticmethod
    def powered() -> str:
        return DDnetApi().domain

    async def player(self, player: str) -> DDPlayer:
        """Fetch player data from the API and return it as a dictionary."""
        return await self._generate_model_instance(
            f"https://{self.domain}/players/?json2={quote(player)}",
            DDPlayer
        )

    async def status(self) -> DDStatus:
        return await self._generate_model_instance(
            f"https://{self.domain}/status/json/stats.json",
            DDStatus
        )

    async def releases_map(self) -> ReleasesMaps:
        return await self._generate_model_instance(
            f"https://{self.domain}/releases/maps.json",
            ReleasesMaps,
            "maps"
        )

    async def query(self, player: str) -> Query:
        return await self._generate_model_instance(
            f"https://{self.domain}/players/?query={quote(player)}",
            Query,
            "players"
        )

    async def query_map(self, map_name: str) -> QueryMap:
        return await self._generate_model_instance(
            f"https://{self.domain}/maps/?query={quote(map_name)}",
            QueryMap,
            'maps',
        )

    async def query_mapper(self, player: str) -> QueryMapper:
        return await self._generate_model_instance(
            f"https://{self.domain}/maps/?qmapper={quote(player)}",
            QueryMapper,
            'players',
        )

    async def master(self, master: MasterEnum = MasterEnum.master1) -> Master:
        return await self._generate_model_instance(
            f"https://{master}.{self.domain}/ddnet/15/servers.json",
            Master
        )

    async def map(self, map_name: str) -> DMap:
        return await self._generate_model_instance(
            f"https://{self.domain}/maps/?json={quote(map_name)}",
            DMap
        )


class DDstats(API):
    def __init__(self):
        super().__init__()
        self.domain = 'ddstats.tw'

    @staticmethod
    def powered() -> str:
        return DDstats().domain

    async def player(self, player_name: str) -> Player:
        """Fetch player data from the API and return it as a dictionary."""
        return await self._generate_model_instance(
            f"https://{self.domain}/player/json?player={quote(player_name)}",
            Player
        )


class Status(API):
    def __init__(self):
        super().__init__()
        self.domain = 'status.tw'

    @staticmethod
    def powered() -> str:
        return Status().domain

    async def info(self) -> None:
        # https://api.status.tw/info
        raise NotImplementedError()

    async def master_bans(self) -> None:
        # https://api.status.tw/master/bans/list
        raise NotImplementedError()

    async def map_list(self) -> None:
        # https://api.status.tw/map/list
        raise NotImplementedError()

    async def map(self, name: str) -> None:
        # https://api.status.tw/map/name/{name}
        raise NotImplementedError()

    async def gametype_list(self) -> None:
        # https://api.status.tw/gametype/list
        raise NotImplementedError()

    async def gametype(self, name: str) -> None:
        # https://api.status.tw/gametype/name/{name}
        raise NotImplementedError()

    async def version_list(self) -> None:
        # https://api.status.tw/version/list
        raise NotImplementedError()

    async def version(self, name: str) -> None:
        # https://api.status.tw/version/name/{name}
        raise NotImplementedError()

    async def server_list(self) -> MasterTw:
        """Fetch player data from the API and return it as a dictionary."""
        return await self._generate_model_instance(
            f"https://api.{self.domain}/server/list",
            MasterTw,
            "servers"
        )

    async def server(self, ip: str, port: Union[int, str]) -> ServerTwOne:
        return await self._generate_model_instance(
            f"https://api.{self.domain}/server/{quote(ip)}/{port}",
            ServerTwOne,
        )

    async def server_charts(self, ip: str, port: Union[int, str], chart: ChartEnum = ChartEnum.day) -> Charts:
        return await self._generate_model_instance(
            f"https://api.{self.domain}/server/{quote(ip)}/{port}/chart/{chart}",
            Charts,
            "charts"
        )

    async def server_history(self, ip: str, port: Union[int, str]) -> None:
        # https://api.status.tw/server/{ip}/{port}/history
        raise NotImplementedError()

    async def server_stats(self, ip: str, port: Union[int, str]) -> None:
        # https://api.status.tw/server/{ip}/{port}/stats
        raise NotImplementedError()

    async def clan_list(self) -> None:
        # https://api.status.tw/clan/list
        raise NotImplementedError()

    async def clan(self, name: str) -> None:
        # https://api.status.tw/clan/name/{name}
        raise NotImplementedError()

    async def player_list(self) -> None:
        # https://api.status.tw/player/list
        raise NotImplementedError()

    async def player(self, name: str) -> None:
        # https://api.status.tw/player/name/{name}
        raise NotImplementedError()

    async def player_history(self, name: str) -> None:
        # https://api.status.tw/player/name/{name}/history
        raise NotImplementedError()

    async def stats(self) -> None:
        # https://api.status.tw/stats
        raise NotImplementedError()

    async def stats_players(self, t: str) -> None:
        # https://api.status.tw/stats/players/day week month
        raise NotImplementedError()

    async def stats_servers(self, t: str) -> None:
        # https://api.status.tw/stats/servers/week month
        raise NotImplementedError()
