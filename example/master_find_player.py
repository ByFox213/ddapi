import asyncio
from ddapi import DDnetApi, Master


async def main():
    obj = DDnetApi()
    player = "ByFox"
    master: Master = await obj.master()
    async for info in master.get_info():
        for client in info.clients:
            if player == client.name:
                print(f'{info.name}: {player}')
    await obj.close()  # Closing client Not necessary
    assert isinstance(master, Master)


asyncio.run(main())
