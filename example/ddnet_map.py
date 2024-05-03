import asyncio
from ddapi import DDnetApi, DMap


async def main():
    obj = DDnetApi()
    dd_map: DMap = await obj.map("Just Fly 13")
    if dd_map is None:
        await obj.close()
        return "Map not found"
    print(f"{dd_map.name}: {dd_map.points}")
    print(dd_map.ranks[0].time)
    await obj.close()  # Closing client Not necessary
    assert isinstance(dd_map, DMap)


asyncio.run(main())
