import json
from unittest import IsolatedAsyncioTestCase

from .base import start_tests
from .config import test_players, _map
from ddapi import DDstats
from ddapi.scheme.ddstats_tw import SMap, DProfile, Player, Maps

start_tests()


class DDstatsTests(IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._test_players = test_players
        self.map = _map
        self.obj = None

    async def asyncSetUp(self) -> None:
        self.obj = DDstats(json_loads=json.loads)

    # DDstats
    async def test_dds_players(self) -> None:
        """Test that player lookups return proper Player instances."""
        for player in self._test_players:
            result = await self.obj.player(player)
            assert isinstance(result, Player), (
                f"Expected Player for {player}, got {type(result)}"
            )

    async def test_dds_maps(self) -> None:
        """Test that maps() returns a valid Maps instance."""
        result = await self.obj.maps()
        assert isinstance(result, Maps), f"Expected Maps, got {type(result)}"

    async def test_dds_map(self) -> None:
        """Test that map lookup returns a valid SMap instance."""
        result = await self.obj.map(self.map)
        assert isinstance(result, SMap), (
            f"Expected SMap for {self.map}, got {type(result)}"
        )

    async def test_dds_profile(self) -> None:
        """Test that profile lookups return proper DProfile instances."""
        for player in self._test_players:
            result = await self.obj.profile(player)
            assert isinstance(result, DProfile), (
                f"Expected DProfile for {player}, got {type(result)}"
            )
