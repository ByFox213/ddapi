import asyncio

from ddapi import DDnetApi


async def main() -> None:
    async with DDnetApi() as obj:
        status = await obj.status()
    if status is not None:
        for server in status.servers:
            percent = round(server.memory_used / server.memory_total * 100, 2)
            print(f"{server.name}. cpu: {server.cpu} | memory: {percent}%")
    else:
        print("Error response")


asyncio.run(main())
