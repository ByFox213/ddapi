from unittest import IsolatedAsyncioTestCase

from .config import test_players, _map
from ddapi import DDnetApi
from ddapi.scheme.ddnet import (
    DDPlayer,
    DMap,
    Master,
    Query,
    QueryMap,
    ReleasesMaps,
    QueryMapper,
    DDStatus,
)


class DDnetTests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_players = test_players
        self.map = _map
        self.obj = None

    async def asyncSetUp(self):
        self.obj = DDnetApi()

    async def asyncTearDown(self):
        await self.obj.close()

    async def test_players(self):
        for player in self._test_players:
            self.assertIsInstance(await self.obj.player(player), DDPlayer)

    async def test_map(self):
        self.assertIsInstance(await self.obj.map("Just Fly 1"), DMap)

    async def test_master(self):
        self.assertIsInstance(await self.obj.master(), Master)

    async def test_query(self):
        self.assertIsInstance(await self.obj.query("ByFox"), Query)

    async def test_query_map(self):
        self.assertIsInstance(await self.obj.query_map("Equivalent"), QueryMap)

    async def test_releases_map(self):
        self.assertIsInstance(await self.obj.releases_map(), ReleasesMaps)

    async def test_query_mapper(self):
        self.assertIsInstance(await self.obj.query_mapper("Quix"), QueryMapper)

    async def test_status(self):
        self.assertIsInstance(await self.obj.status(), DDStatus)
