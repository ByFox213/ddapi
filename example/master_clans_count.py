import asyncio

from ddapi import DDnetApi, Master


async def main():
    async with DDnetApi() as obj:
        master: Master = await obj.master()
    print(master.get_clans()[:10])


asyncio.run(main())
