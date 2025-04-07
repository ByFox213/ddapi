from unittest import IsolatedAsyncioTestCase

from config import test_players, _map
from ddapi import DDnetApi
from ddapi.scheme.ddnet import DDPlayer, DMap, Master, Query, QueryMap, ReleasesMaps, QueryMapper, DDStatus


class DDnetTests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_players = test_players
        self.map = _map

    async def test_players(self):
        dd = DDnetApi()
        for player in self._test_players:
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
