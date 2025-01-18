import asyncio

from ddapi import DDnetApi, DMap


async def main():
    obj = DDnetApi()
    dd_map: DMap = await obj.map("Just Fly 1")
    if dd_map is None:
        await obj.close()
        print("Map not found |", dd_map)
        return
    print(f"{dd_map.name}: {dd_map.points}")
    print(dd_map.ranks[0].time)
    await obj.close()  # Closing client Not necessary
    assert isinstance(dd_map, DMap)


asyncio.run(main())
