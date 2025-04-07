from unittest import IsolatedAsyncioTestCase

from config import ip, port
from ddapi import Status
from ddapi.scheme.status_tw import MasterTw, Info, BannedMaster, List, ListData, ListPl, ListPlData, ServerTwOne, \
    Charts, ChartEnum


class StatsTests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ip = ip
        self.port = port

    async def test_status_server_list(self):
        dd = Status()
        self.assertIsInstance(
            await dd.server_list(),
            MasterTw
        )
        await dd.close()

    async def test_status_info(self):
        dd = Status()
        self.assertIsInstance(
            await dd.info(),
            Info
        )
        await dd.close()

    async def test_status_master_bans(self):
        dd = Status()
        self.assertIsInstance(
            await dd.master_bans(),
            BannedMaster
        )
        await dd.close()

    async def test_status_map_list(self):
        dd = Status()
        self.assertIsInstance(
            await dd.map_list(),
            List
        )
        await dd.close()

    async def test_status_map(self):
        dd = Status()
        self.assertIsInstance(
            await dd.map("Baby Aim 1.0"),
            ListData
        )
        await dd.close()

    async def test_status_gametype_list(self):
        dd = Status()
        self.assertIsInstance(
            await dd.gametype_list(),
            List
        )
        await dd.close()

    async def test_status_gametype(self):
        dd = Status()
        self.assertIsInstance(
            await dd.gametype("DDraceNetwork"),
            ListData
        )
        await dd.close()

    async def test_status_version_list(self):
        dd = Status()
        self.assertIsInstance(
            await dd.version_list(),
            List
        )
        await dd.close()

    async def test_status_version(self):
        dd = Status()
        self.assertIsInstance(
            await dd.version("0.6.4, 19.1"),
            ListData
        )
        await dd.close()

    async def test_status_player_list(self):
        dd = Status()
        self.assertIsInstance(
            await dd.player_list(),
            ListPl
        )
        await dd.close()

    async def test_status_player(self):
        dd = Status()
        self.assertIsInstance(
            await dd.player("ByFox"),
            ListPlData
        )
        await dd.close()

    async def test_status_clan_list(self):
        dd = Status()
        self.assertIsInstance(
            await dd.clan_list(),
            ListPl
        )
        await dd.close()

    async def test_status_clan(self):
        dd = Status()
        self.assertIsInstance(
            await dd.clan("63 turtles"),
            ListPlData
        )
        await dd.close()

    async def test_status_server(self):
        dd = Status()
        self.assertIsInstance(
            await dd.server(self.ip, self.port),
            ServerTwOne
        )
        await dd.close()

    async def test_status_chart(self):
        dd = Status()
        self.assertIsInstance(
            await dd.server_charts(self.ip, self.port, ChartEnum.week),
            Charts
        )  # week
        self.assertIsInstance(
            await dd.server_charts(self.ip, self.port, ChartEnum.month),
            Charts
        )  # month
        await dd.close()
