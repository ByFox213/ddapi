from typing import Union
from urllib.parse import quote

from .deflt import API
from .scheme import DDPlayer, Master, Query, DMap, DDStatus, Player, MasterTw

__all__ = (
    "DDnetApi",
    "DDstats",
    "Status"
)


class DDnetApi(API):
    def __init__(self):
        super().__init__()
        self.domain = "ddnet.org"

    @staticmethod
    def powered() -> str:
        return DDnetApi().domain

    async def player(self, player_name: str) -> DDPlayer:
        """Fetch player data from the API and return it as a dictionary."""
        return await self._generate_model_instance(
            f"https://{self.domain}/players/?json2={quote(player_name)}",
            DDPlayer
        )

    async def status(self) -> Union[DDStatus, None]:
        return await self._generate_model_instance(
            f"https://{self.domain}/status/json/stats.json",
            DDStatus
        )

    async def query(self, player: str) -> Union[Query, None]:
        return await self._generate_model_instance(
            f"https://{self.domain}/players/?query={quote(player)}",
            Query,
            "data"
        )

    async def master(self) -> Union[Master, None]:
        return await self._generate_model_instance(
            f"https://master1.{self.domain}/ddnet/15/servers.json",
            Master
        )

    async def map(self, map_name: str) -> Union[DMap, None]:
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


class Status(API):  # TODO: Add other
    def __init__(self):
        super().__init__()
        self.domain = 'status.tw'

    @staticmethod
    def powered() -> str:
        return Status().domain

    async def server_list(self) -> MasterTw:
        """Fetch player data from the API and return it as a dictionary."""
        return await self._generate_model_instance(
            f"https://api.{self.domain}/server/list",
            MasterTw,
            "servers"
        )
