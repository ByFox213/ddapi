import asyncio

from ddapi import DDnetApi, Master


async def main():
    obj = DDnetApi()
    player = "nameless tee"
    master: Master = await obj.master()
    for server in master.servers:
        for client in server.info.clients:
            if player == client.name:
                print(f'{server.info.name}: {player}')
    await obj.close()  # Closing client Not necessary
    assert isinstance(master, Master)


asyncio.run(main())
