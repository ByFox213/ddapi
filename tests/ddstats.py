from unittest import IsolatedAsyncioTestCase

from .config import test_players, _map
from ddapi import DDstats
from ddapi.scheme.ddstats_tw import SMap, DProfile, Player, Maps


class DDstatsTests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_players = test_players
        self.map = _map
        self.obj = None

    async def asyncSetUp(self):
        self.obj = DDstats()

    async def asyncTearDown(self):
        await self.obj.close()

    # DDstats
    async def test_dds_players(self):
        for player in self._test_players:
            self.assertIsInstance(await self.obj.player(player), Player)

    async def test_dds_maps(self):
        self.assertIsInstance(await self.obj.maps(), Maps)

    async def test_dds_map(self):
        self.assertIsInstance(await self.obj.map(self.map), SMap)

    async def test_dds_profile(self):
        for player in self._test_players:
            self.assertIsInstance(await self.obj.profile(player), DProfile)
