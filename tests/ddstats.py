from unittest import IsolatedAsyncioTestCase

from config import test_players, _map
from ddapi import DDstats
from ddapi.scheme.ddstats_tw import SMap, DProfile, Player, Maps


class DDstatsTests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_players = test_players
        self.map = _map

    # DDstats
    async def test_dds_players(self):
        dds = DDstats()
        for player in self._test_players:
            self.assertIsInstance(
                await dds.player(player),
                Player
            )
        await dds.close()

    async def test_dds_maps(self):
        dds = DDstats()
        self.assertIsInstance(
            await dds.maps(),
            Maps
        )
        await dds.close()

    async def test_dds_map(self):
        dds = DDstats()
        self.assertIsInstance(
            await dds.map(self.map),
            SMap
        )
        await dds.close()

    async def test_dds_profile(self):
        dds = DDstats()
        for player in self._test_players:
            self.assertIsInstance(
                await dds.profile(player),
                DProfile
            )
        await dds.close()
