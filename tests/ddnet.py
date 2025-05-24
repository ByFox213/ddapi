import json
from unittest import IsolatedAsyncioTestCase

from .base import start_tests
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

start_tests()


class DDnetTests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._test_players = test_players
        self.map = _map
        self.obj = None

    async def asyncSetUp(self) -> None:
        self.obj = DDnetApi(json_loads=json.loads)

    async def test_players(self) -> None:
        """Verify player lookups return DDPlayer instances."""
        for player in self._test_players:
            result = await self.obj.player(player)
            assert isinstance(result, DDPlayer), (
                f"Expected DDPlayer for {player}, got {type(result).__name__}"
            )

    async def test_map(self) -> None:
        """Test map lookup returns DMap instance."""
        result = await self.obj.map("Just Fly 1")
        assert isinstance(result, DMap), f"Expected DMap, got {type(result).__name__}"

    async def test_master(self) -> None:
        """Verify master server response type."""
        result = await self.obj.master()
        assert isinstance(result, Master), (
            f"Expected Master, got {type(result).__name__}"
        )

    async def test_query(self) -> None:
        """Test player query returns Query instance."""
        result = await self.obj.query("ByFox")
        assert isinstance(result, Query), f"Expected Query, got {type(result).__name__}"

    async def test_query_map(self) -> None:
        """Test map query returns QueryMap instance."""
        result = await self.obj.query_map("Equivalent")
        assert isinstance(result, QueryMap), (
            f"Expected QueryMap, got {type(result).__name__}"
        )

    async def test_releases_map(self) -> None:
        """Verify map releases response type."""
        result = await self.obj.releases_map()
        assert isinstance(result, ReleasesMaps), (
            f"Expected ReleasesMaps, got {type(result).__name__}"
        )

    async def test_query_mapper(self) -> None:
        """Test mapper query returns QueryMapper instance."""
        result = await self.obj.query_mapper("Quix")
        assert isinstance(result, QueryMapper), (
            f"Expected QueryMapper, got {type(result).__name__}"
        )

    async def test_status(self) -> None:
        """Verify server status response type."""
        result = await self.obj.status()
        assert isinstance(result, DDStatus), (
            f"Expected DDStatus, got {type(result).__name__}"
        )
