import asyncio
from ddapi import DDnetApi, Master


async def main():
    obj = DDnetApi()
    master: Master = await obj.master()
    print(master.get_clans(10))  # default: 50
    await obj.close()  # Closing client Not necessary
    assert isinstance(master, Master)


asyncio.run(main())
