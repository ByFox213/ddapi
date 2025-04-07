import asyncio

from ddapi import DDstats


async def main():
    async with DDstats() as obj:
        user = await obj.player("ByFox")
    if user is not None:
        print(f"{user.profile.name=}")
        print(f"{user.profile.clan=}")
        print(f"{user.general_activity.total_seconds_played=}")


asyncio.run(main())
