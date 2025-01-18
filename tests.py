from unittest import IsolatedAsyncioTestCase

from ddapi import DDnetApi, DDstats, Player, DMap, DDPlayer, Query, Master, DDStatus, MasterTw, Status, ServerTwOne, \
    ChartEnum, Charts


class Tests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_players = [
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

    async def test_dds_players(self):
        dds = DDstats()
        for player in self.test_players:
            self.assertIsInstance(
                await dds.player(player),
                Player
            )
        await dds.close()

    async def test_players(self):
        dd = DDnetApi()
        for player in self.test_players:
            self.assertIsInstance(
                await dd.player(player),
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

    async def test_status(self):
        dd = DDnetApi()
        self.assertIsInstance(
            await dd.status(),
            DDStatus
        )
        await dd.close()

    async def test_status_server_list(self):
        dd = Status()
        self.assertIsInstance(
            await dd.server_list(),
            MasterTw
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
