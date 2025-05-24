import json
from unittest import IsolatedAsyncioTestCase

from .base import start_tests
from .config import ip, port
from ddapi import Status
from ddapi.scheme.status_tw import (
    MasterTw,
    Info,
    BannedMaster,
    List,
    ListData,
    ListPl,
    ListPlData,
    ServerTwOne,
    Charts,
    ChartEnum,
)

start_tests()


class StatsTests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ip = ip
        self.port = port
        self.obj = None

    async def asyncSetUp(self) -> None:
        self.obj = Status(json_loads=json.loads)

    async def test_status_server_list(self) -> None:
        assert isinstance(await self.obj.server_list(), MasterTw)

    async def test_status_info(self) -> None:
        assert isinstance(await self.obj.info(), Info)

    async def test_status_master_bans(self) -> None:
        assert isinstance(await self.obj.master_bans(), BannedMaster)

    async def test_status_map_list(self) -> None:
        result = await self.obj.map_list()
        assert isinstance(result, List), f"Expected List, got {type(result)}"

    async def test_status_map(self) -> None:
        result = await self.obj.map("Baby Aim 1.0")
        assert isinstance(result, ListData), f"Expected ListData, got {type(result)}"

    async def test_status_gametype_list(self) -> None:
        result = await self.obj.gametype_list()
        assert isinstance(result, List), f"Expected List, got {type(result)}"

    async def test_status_gametype(self) -> None:
        result = await self.obj.gametype("DDraceNetwork")
        assert isinstance(result, ListData), f"Expected ListData, got {type(result)}"

    async def test_status_version_list(self) -> None:
        result = await self.obj.version_list()
        assert isinstance(result, List), f"Expected List, got {type(result)}"

    async def test_status_version(self) -> None:
        result = await self.obj.version("0.6.4, 19.1")
        assert isinstance(result, ListData), f"Expected ListData, got {type(result)}"

    async def test_status_player_list(self) -> None:
        result = await self.obj.player_list()
        assert isinstance(result, ListPl), f"Expected ListPl, got {type(result)}"

    async def test_status_player(self) -> None:
        result = await self.obj.player("ByFox")
        assert isinstance(result, ListPlData), (
            f"Expected ListPlData, got {type(result)}"
        )

    async def test_status_clan_list(self) -> None:
        result = await self.obj.clan_list()
        assert isinstance(result, ListPl), f"Expected ListPl, got {type(result)}"

    async def test_status_clan(self) -> None:
        result = await self.obj.clan("63 turtles")
        assert isinstance(result, ListPlData), (
            f"Expected ListPlData, got {type(result)}"
        )

    async def test_status_server(self) -> None:
        result = await self.obj.server(self.ip, self.port)
        assert isinstance(result, ServerTwOne), (
            f"Expected ServerTwOne, got {type(result)}"
        )

    async def test_status_chart(self) -> None:
        for chart_type in [ChartEnum.week, ChartEnum.month]:
            result = await self.obj.server_charts(self.ip, self.port, chart_type)
            assert isinstance(result, Charts), f"Failed for {chart_type.name}"
