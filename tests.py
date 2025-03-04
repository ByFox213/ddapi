from unittest import IsolatedAsyncioTestCase

from ddapi import DDnetApi, DDstats, Player, DMap, DDPlayer, Query, Master, DDStatus, MasterTw, Status, ServerTwOne, \
    ChartEnum, Charts, QueryMapper, QueryMap, ReleasesMaps, Info, BannedMaster, List, ListData, ListPl, ListPlData


class Tests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_players = [
            "ByFox",
            "Cor",
            "Freezestyler",
            "<BµmM>",
            "Aoe",
            "Gazebr",
            "ban+eblan"
        ]
        self.ip = "45.141.57.22"
        self.port = 8303

    # DDnetApi
    async def test_players(self):
        dd = DDnetApi()
        for player in self._test_players:
            result = await dd.player(player)
            self.assertIsInstance(
                result,
                DDPlayer
            )
        await dd.close()

    async def test_map(self):
        dd = DDnetApi()
        self.assertIsInstance(
            await dd.map("Just Fly 1"),
            DMap
        )
        await dd.close()

    async def test_master(self):
        dd = DDnetApi()
        self.assertIsInstance(
            await dd.master(),
            Master
        )
        await dd.close()

    async def test_query(self):
        dd = DDnetApi()
        self.assertIsInstance(
            await dd.query("ByFox"),
            Query
        )
        await dd.close()

    async def test_query_map(self):
        dd = DDnetApi()
        self.assertIsInstance(
            await dd.query_map("Equivalent"),
            QueryMap
        )
        await dd.close()

    async def test_releases_map(self):
        dd = DDnetApi()
        self.assertIsInstance(
            await dd.releases_map(),
            ReleasesMaps
        )
        await dd.close()

    async def test_query_mapper(self):
        dd = DDnetApi()
        self.assertIsInstance(
            await dd.query_mapper("Quix"),
            QueryMapper
        )
        await dd.close()

    async def test_status(self):
        dd = DDnetApi()
        self.assertIsInstance(
            await dd.status(),
            DDStatus
        )
        await dd.close()

    # DDstats
    async def test_dds_players(self):
        dds = DDstats()
        for player in self._test_players:
            self.assertIsInstance(
                await dds.player(player),
                Player
            )
            print(player)
        await dds.close()

    # Status
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
            List
        )
        await dd.close()

    async def test_status_clan(self):
        dd = Status()
        self.assertIsInstance(
            await dd.clan("63 turtles"),
            ListData
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
