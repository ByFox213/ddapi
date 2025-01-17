from unittest import IsolatedAsyncioTestCase

from ddapi import DDnetApi, DDstats, Player, DMap, DDPlayer, Query, Master, DDStatus, MasterTw, Status


class Tests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_player = ["ByFox", "Cor", "Freezestyler", "<BµmM>", "Aoe", "Gazebr", "ban+eblan"]

    async def test_dds_players(self):
        dds = DDstats()
        for player in self.test_player:
            result = await dds.player(player)
            self.assertIsInstance(result, Player)
        self.assertNotIsInstance(
            await dds.player("RandomNicknameRRRRRRRRR"), Player
        )
        await dds.close()

    async def test_players(self):
        dd = DDnetApi()
        for player in self.test_player:
            result = await dd.player(player)
            self.assertIsInstance(result, DDPlayer)
        self.assertNotIsInstance(
            await dd.player("RandomNicknameRRRRRRRRR"), DDPlayer
        )
        await dd.close()

    async def test_map(self):
        dd = DDnetApi()
        self.assertIsInstance(
            await dd.map("Just Fly 1"), DMap
        )
        self.assertNotIsInstance(
            await dd.map("Just Fly"), DMap
        )
        await dd.close()

    async def test_master(self):
        dd = DDnetApi()
        result = await dd.master()
        self.assertIsInstance(result, Master)
        await dd.close()

    async def test_query(self):
        dd = DDnetApi()
        result = await dd.query("ByFox")
        self.assertIsInstance(result, Query)
        await dd.close()

    async def test_status(self):
        dd = DDnetApi()
        result = await dd.status()
        self.assertIsInstance(result, DDStatus)
        await dd.close()

    async def test_status_server_list(self):
        dd = Status()
        result = await dd.server_list()
        self.assertIsInstance(result, MasterTw)
        await dd.close()


