# Status.tw
from datetime import datetime

from pydantic import BaseModel


class DataTw(BaseModel):
    name: str
    createdAt: datetime

class VersionTw(BaseModel):
    version: str
    createdAt: datetime


class CountryTw(BaseModel):
    identifier: str
    code: int
    iconUrl: str


class ClientTw(BaseModel):
    name: str
    country: CountryTw
    score: int
    isPlayer: bool
    isAfk: bool
    team: int
    createdAt: datetime
    clan: DataTw | None


class ServersTw(BaseModel):
    ip: str
    port: int
    name: str
    numClients: int
    numPlayers: int
    maxClients: int
    maxPlayers: int
    hasPassword: bool
    supports6: bool
    supports7: bool
    createdAt: datetime
    relevanceScore: int
    clientScoreKind: str | None
    logoUrl: str
    map: DataTw
    website: str | None = None
    discordInvite: str | None = None
    description: str | None = None
    gameType: DataTw
    version: VersionTw
    clients: list[ClientTw]


class MasterTw(BaseModel):
    servers: list[ServersTw]