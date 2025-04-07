import asyncio

from ddapi import DDnetApi, Master


async def main():
    async with DDnetApi() as obj:
        master: Master = await obj.master()

    nickname = "nameless tee"
    for server in master.servers:
        for client in server.info.clients:
            if nickname != client.name:
                continue
            print(f"{server.info.name}: {nickname}")


asyncio.run(main())
