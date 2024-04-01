# pylint: disable-all
from collections import Counter
from typing import Optional, Union, Any

from pydantic import BaseModel, Field


# ddnet
class DPoints(BaseModel):
    total: Optional[int] = Field(default=None)
    points: Optional[int] = Field(default=None)
    rank: Optional[int] = Field(default=None)


class DRank(BaseModel):
    points: Optional[int] = Field(default=None)
    rank: Optional[int] = Field(default=None)


class FirstFinish(BaseModel):
    timestamp: Optional[float] = Field(default=None)
    map: Optional[str] = Field(default=None)
    time: Optional[float] = Field(default=None)


class LastFinish(BaseModel):
    timestamp: Optional[float] = Field(default=None)
    map: Optional[str] = Field(default=None)
    time: Optional[float] = Field(default=None)
    country: Optional[str] = Field(default=None)
    type: Optional[str] = Field(default=None)


class FavorPart(BaseModel):
    name: Optional[str] = Field(default=None)
    finishes: Optional[int] = Field(default=None)


class DData(BaseModel):
    points: Optional[DPoints] = Field(default=None)
    team_rank: Optional[DRank] = Field(default=None)
    rank: Optional[DRank] = Field(default=None)
    maps: Optional[dict] = Field(default=None)


class DDType(BaseModel):
    Novice: Optional[DData] = Field(default=None)
    Moderate: Optional[DData] = Field(default=None)
    Brutal: Optional[DData] = Field(default=None)
    Insane: Optional[DData] = Field(default=None)
    Dummy: Optional[DData] = Field(default=None)
    DDmaX_Easy: Optional[DData] = Field(default=None, validation_alias='DDmaX.Easy')
    DDmaX_Next: Optional[DData] = Field(default=None, validation_alias='DDmaX.Next')
    DDmaX_Nut: Optional[DData] = Field(default=None, validation_alias='DDmaX.Nut')
    DDmaX_Pro: Optional[DData] = Field(default=None, validation_alias='DDmaX.Pro')
    Oldschool: Optional[DData] = Field(default=None)
    Race: Optional[DData] = Field(default=None)
    Solo: Optional[DData] = Field(default=None)
    total: Optional[DData] = Field(default=None)


class DActiov(BaseModel):
    date: Optional[str] = Field(default=None)
    hours_played: Optional[int] = Field(default=None)


class DDPlayer(BaseModel):
    emoji: Any = Field(default=None)
    player: Optional[str] = Field(default=None)
    points: Optional[DPoints] = Field(default=None)
    team_rank: Optional[DRank] = Field(default=None)
    rank: Optional[DRank] = Field(default=None)
    points_last_month: Optional[DRank] = Field(default=None)
    points_last_week: Optional[DRank] = Field(default=None)
    first_finish: Optional[FirstFinish] = Field(default=None)
    last_finishes: Optional[list[LastFinish]] = Field(default=None)
    favorite_partners: Optional[list[FavorPart]] = Field(default=None)
    types: Optional[DDType] = Field(default=None)
    activity: Optional[list[DActiov]] = Field(default=None)
    hours_played_past_365_days: Optional[int] = Field(default=None)


# qwik
class Skin(BaseModel):
    name: Optional[str] = Field(default=None)
    color_body: Optional[int] = Field(default=None)
    color_feet: Optional[int] = Field(default=None)


class PData(BaseModel):
    rank: Optional[int] = Field(default=None)
    points: Optional[int] = Field(default=None)


class PPoints(BaseModel):
    Novice: Optional[PData] = Field(default=None)
    Moderate: Optional[PData] = Field(default=None)
    Brutal: Optional[PData] = Field(default=None)
    Insane: Optional[PData] = Field(default=None)
    Dummy: Optional[PData] = Field(default=None)
    DDmaX_Easy: Optional[PData] = Field(default=None, validation_alias='DDmaX.Easy')
    DDmaX_Next: Optional[PData] = Field(default=None, validation_alias='DDmaX.Next')
    DDmaX_Nut: Optional[PData] = Field(default=None, validation_alias='DDmaX.Nut')
    DDmaX_Pro: Optional[PData] = Field(default=None, validation_alias='DDmaX.Pro')
    Oldschool: Optional[PData] = Field(default=None)
    Race: Optional[PData] = Field(default=None)
    Solo: Optional[PData] = Field(default=None)
    total: Optional[PData] = Field(default=None)


class Points(BaseModel):
    points: Optional[PPoints] = Field(default=None)
    rankpoints: Optional[PPoints] = Field(default=None)
    teampoints: Optional[PPoints] = Field(default=None)


class RData(BaseModel):
    Map: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Time: Optional[float] = Field(default=None)
    Server: Optional[str] = Field(default=None)
    Rank: Optional[int] = Field(default=None)
    Teamrank: Optional[int] = Field(default=None)
    Category: str
    Points: int


class Rankings(BaseModel):
    Novice: Optional[list[RData]] = Field(default=None)
    Moderate: Optional[list[RData]] = Field(default=None)
    Brutal: Optional[list[RData]] = Field(default=None)
    Insane: Optional[list[RData]] = Field(default=None)
    Dummy: Optional[list[RData]] = Field(default=None)
    DDmaX_Easy: Optional[list[RData]] = Field(default=None, validation_alias='DDmaX.Easy')
    DDmaX_Next: Optional[list[RData]] = Field(default=None, validation_alias='DDmaX.Next')
    DDmaX_Nut: Optional[list[RData]] = Field(default=None, validation_alias='DDmaX.Nut')
    DDmaX_Pro: Optional[list[RData]] = Field(default=None, validation_alias='DDmaX.Pro')
    Oldschool: Optional[list[RData]] = Field(default=None)
    Race: Optional[list[RData]] = Field(default=None)
    Solo: Optional[list[RData]] = Field(default=None)
    Fun: Optional[list[RData]] = Field(default=None)
    total: Optional[list[RData]] = Field(default=None)


class RPointG(BaseModel):
    date: Optional[str] = Field(default=None)
    rankpoints: Optional[int] = Field(default=None)
    teampoints: Optional[int] = Field(default=None)


class PointG(BaseModel):
    date: Optional[str] = Field(default=None)
    points: Optional[int] = Field(default=None)
    maps: Optional[str] = Field(default=None)


class RecentPlayerInfo(BaseModel):
    date: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    clan: Optional[str] = Field(default=None)
    country: Optional[int] = Field(default=None)
    skin_name: Optional[str] = Field(default=None)
    skin_color_body: Optional[int] = Field(default=None)
    skin_color_feet: Optional[int] = Field(default=None)


class RecentPlayTime(BaseModel):
    date: Optional[str] = Field(default=None)
    map: Optional[str] = Field(default=None)
    player: Optional[str] = Field(default=None)
    Playtime: Optional[int] = Field(default=None)
    Server: Optional[str] = Field(default=None)


class PlaytimeCategories(BaseModel):
    Category: Optional[str] = Field(default=None)
    Playtime: Optional[int] = Field(default=None)


class PlaytimeGameTypes(BaseModel):
    gametype: Optional[str] = Field(default=None)
    Playtime: Optional[int] = Field(default=None)


class PlaytimeLocation(BaseModel):
    location: Optional[str] = Field(default=None)
    Playtime: Optional[int] = Field(default=None)


class PlaytimePerMonth(BaseModel):
    Year: Optional[str] = Field(default=None)
    Month: Optional[str] = Field(default=None)
    Playtime: Optional[int] = Field(default=None)


class MostPlayedMaps(BaseModel):
    map: Optional[str] = Field(default=None)
    Server: Optional[str] = Field(default=None)
    Playtime: Optional[int] = Field(default=None)


class AllTop10s(BaseModel):
    Server: Optional[str] = Field(default=None)
    Map: Optional[str] = Field(default=None)
    rank: Optional[int] = Field(default=None)
    rtime: Optional[float] = Field(default=None)
    teamrank: Optional[int] = Field(default=None)
    ttime: Optional[float] = Field(default=None)


class AmountOfTop10(BaseModel):
    Name: Optional[str] = Field(default=None)
    Rank: Optional[int] = Field(default=None)
    RankAmount: Optional[int] = Field(default=None)
    TeamRankAmount: Optional[int] = Field(default=None)


class Rank1sPartners(BaseModel):
    Name: Optional[str] = Field(default=None)
    Amount: Optional[int] = Field(default=None)


class RecentTop10s(BaseModel):
    Timestamp: Optional[str] = Field(default=None)
    Server: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Time: Optional[float] = Field(default=None)
    Map: Optional[str] = Field(default=None)
    Rank: Optional[int] = Field(default=None)


class Player(BaseModel):
    player: Optional[str] = Field(default=None)
    clan: Optional[str] = Field(default=None)
    country: Optional[int] = Field(default=None)
    skin: Optional[Skin] = Field(default=None)
    stamp: Optional[str] = Field(default=None)
    points: Optional[Points] = Field(default=None)
    rankings: Optional[Rankings] = Field(default=None)
    isMapper: Optional[int] = Field(default=None)
    rankedPointsGraph: Optional[list[RPointG]] = Field(default=None)
    pointsGraph: Optional[list[PointG]] = Field(default=None)
    playtime: Optional[dict] = Field(default=None)
    recentPlayerinfo: Optional[list[RecentPlayerInfo]] = Field(default=None)
    recentPlaytime: Optional[list[RecentPlayTime]] = Field(default=None)
    playtimeCategories: Optional[list[PlaytimeCategories]] = Field(default=None)
    playtimeGametypes: Optional[list[PlaytimeGameTypes]] = Field(default=None)
    playtimeLocation: Optional[list[PlaytimeLocation]] = Field(default=None)
    playtimePerMonth: Optional[list[PlaytimePerMonth]] = Field(default=None)
    mostPlayedMaps: Optional[list[MostPlayedMaps]] = Field(default=None)
    allTop10s: Optional[list[AllTop10s]] = Field(default=None)
    AmountOfTop10Placements: Optional[list[AmountOfTop10]] = Field(default=None,
                                                                   validation_alias="AmountOfTop10Placements")
    rank1sPartners: Optional[list[Rank1sPartners]] = Field(default=None)
    recentTop10s: Optional[list[RecentTop10s]] = Field(default=None)


class Client(BaseModel):
    name: str = Field(default='')
    clan: str = Field(default='')
    country: int = Field(default=-1)
    score: int = Field(default=-9999)
    is_player: bool = Field(default=None)
    skin: dict = Field(default=None)
    afk: bool = Field(default=None)
    team: int = Field(default=0)


class Info(BaseModel):
    max_clients: int = Field(default=0)
    max_players: int = Field(default=0)
    passworded: bool = Field(default=None)
    game_type: str = Field(default=None)
    name: str = Field(default=None)
    map: dict = Field(default=None)
    version: str = Field(default=None)
    clients: list[Client] = Field(default=None)


class Server(BaseModel):
    addresses: Union[list, str] = Field(default=None)
    location: str = Field(default=None)
    info: Info = Field(default=None)


class Master(BaseModel):
    servers: list[Server]

    async def get_info(self):
        for i in self.servers:
            yield i.info

    async def get_clients(self):
        for i in self.servers:
            yield i.info.clients

    @property
    def count(self) -> int:
        return len(self.servers)

    def get_clans(self, limit: int = 50):
        dat = Counter(client.clan for server in self.servers for client in server.info.clients)
        del dat['']
        return sorted(dat.items(), key=lambda x: x[1], reverse=True)[:limit]
