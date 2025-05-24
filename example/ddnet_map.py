import asyncio

from ddapi import DDnetApi, DMap


async def main() -> None:
    async with DDnetApi() as obj:
        dd_map: DMap = await obj.map("Just Fly 1")
    if dd_map is not None:
        print(f"{dd_map.name}: {dd_map.points}")
        print(dd_map.ranks[0].time)
    else:
        print("Map not found |", dd_map)


asyncio.run(main())
