import asyncio
from ddapi import StatusAPI, STPlayer, STServers, STServer, STClients, STClans, STGameTypes, STMaps, STVersions, STBans, \
    STMastersStats


async def main():
    obj = StatusAPI()
    server: STServer = await obj.server("51.89.23.241", 8338)
    player: STPlayer = await obj.player("ByFox")
    servers: STServers = await obj.servers()
    players: STClients = await obj.players()
    clans: STClans = await obj.clans()
    gametypes: STGameTypes = await obj.gametype()
    maps: STMaps = await obj.maps()
    bans: STBans = await obj.bans()
    versions: STVersions = await obj.versions()
    stats: STMastersStats = await obj.masters_stats()
    for i in [player, server, servers, players, clans, gametypes, maps, bans, versions, stats]:
        print(i)

    await obj.close()  # Closing client Not necessary


asyncio.run(main())
