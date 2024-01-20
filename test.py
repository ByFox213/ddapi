import unittest
from ddapi import DDnetApi, QwikAPI, DDPlayer, Player


class Tests(unittest.IsolatedAsyncioTestCase):
    async def test_dd_player(self):
        dd = DDnetApi()
        self.player = await dd.player("ByFox")
        await dd.close()
        self.assertIsInstance(self.player, DDPlayer)

    async def test_qw_player(self):
        qw = QwikAPI()
        self.player = await qw.player("ByFox")
        await qw.close()
        self.assertIsInstance(self.player, Player)

    async def test_dd_master(self):
        dd = DDnetApi()
        self.player = await dd.master()
        await dd.close()
        self.assertIsInstance(self.player, dict)


if __name__ == "__main__":
    unittest.main()
