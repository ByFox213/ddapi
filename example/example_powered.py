import asyncio

from ddapi import DDnetApi


async def main():
    dd = DDnetApi()
    print(f"DDnetApi powered by {dd.powered()}")
    # powered is staticmethod
    # It is not necessary to close the connection as it was not created.


asyncio.run(main())
