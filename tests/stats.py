from unittest import IsolatedAsyncioTestCase

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


class StatsTests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ip = ip
        self.port = port
        self.obj = None

    async def asyncSetUp(self):
        self.obj = Status()

    async def asyncTearDown(self):
        await self.obj.close()

    async def test_status_server_list(self):
        self.assertIsInstance(await self.obj.server_list(), MasterTw)

    async def test_status_info(self):
        self.assertIsInstance(await self.obj.info(), Info)

    async def test_status_master_bans(self):
        self.assertIsInstance(await self.obj.master_bans(), BannedMaster)

    async def test_status_map_list(self):
        self.assertIsInstance(await self.obj.map_list(), List)

    async def test_status_map(self):
        self.assertIsInstance(await self.obj.map("Baby Aim 1.0"), ListData)

    async def test_status_gametype_list(self):
        self.assertIsInstance(await self.obj.gametype_list(), List)

    async def test_status_gametype(self):
        self.assertIsInstance(await self.obj.gametype("DDraceNetwork"), ListData)

    async def test_status_version_list(self):
        self.assertIsInstance(await self.obj.version_list(), List)

    async def test_status_version(self):
        self.assertIsInstance(await self.obj.version("0.6.4, 19.1"), ListData)

    async def test_status_player_list(self):
        self.assertIsInstance(await self.obj.player_list(), ListPl)

    async def test_status_player(self):
        self.assertIsInstance(await self.obj.player("ByFox"), ListPlData)

    async def test_status_clan_list(self):
        self.assertIsInstance(await self.obj.clan_list(), ListPl)

    async def test_status_clan(self):
        self.assertIsInstance(await self.obj.clan("63 turtles"), ListPlData)

    async def test_status_server(self):
        self.assertIsInstance(await self.obj.server(self.ip, self.port), ServerTwOne)

    async def test_status_chart(self):
        self.assertIsInstance(
            await self.obj.server_charts(self.ip, self.port, ChartEnum.week), Charts
        )  # week
        self.assertIsInstance(
            await self.obj.server_charts(self.ip, self.port, ChartEnum.month), Charts
        )  # month
