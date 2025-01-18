import asyncio

from ddapi import DDnetApi


async def main():
    obj = DDnetApi()
    status = await obj.status()
    if status is None:
        return await obj.close()

    status = status.servers[0]
    print(f"{status.name}. cpu: {status.cpu}")
    await obj.close()  # Closing client Not necessary


asyncio.run(main())
