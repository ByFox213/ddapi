import asyncio

from ddapi import DDnetApi


async def main():
    # powered is staticmethod
    # It is not necessary to close the connection as it was not created.
    print(f"{DDnetApi.powered()=}")


asyncio.run(main())
