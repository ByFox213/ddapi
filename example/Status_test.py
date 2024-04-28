import asyncio
from ddapi import StatusAPI, STPlayer, STServers, STServer, STClients, STClans, STGameTypes, STMaps, STVersions, STBans, \
    STMastersStats


async def main():
    obj = StatusAPI()
    
    server: STServer = await obj.server("51.89.23.241", 8338)
    print(server)

    player: STPlayer = await obj.player("ByFox")
    print(player)

    servers: STServers = await obj.servers()
    print(servers)

    players: STClients = await obj.players()
    print(players)

    clans: STClans = await obj.clans()
    print(clans)

    gametypes: STGameTypes = await obj.gametype()
    print(gametypes)

    maps: STMaps = await obj.maps()
    print(maps)

    bans: STBans = await obj.bans()
    print(bans)

    versions: STVersions = await obj.versions()
    print(versions)

    stats: STMastersStats = await obj.masters_stats()
    print(stats)

    await obj.close()  # Closing client Not necessary


asyncio.run(main())
