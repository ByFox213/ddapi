import asyncio
from ddapi import DDStats, DDStatsSql


async def main():
    obj = DDStats()

    # all maps(limit 100)
    dd_map: DDStatsSql = await obj.maps()
    if dd_map is None:
        await obj.close()
        return
    print(dd_map.rows)
    # limit 101, 200
    new_dd_map = await obj.next(dd_map)
    print(new_dd_map.rows)

    # get map
    dd = await obj.get_map("luminati")
    print(dd.rows)
    await obj.close()  # Closing client Not necessary


asyncio.run(main())
