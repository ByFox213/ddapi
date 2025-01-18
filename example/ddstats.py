import asyncio

from ddapi import Player, DDstats


async def main():
    obj = DDstats()
    nickname = "ByFox"
    user = await obj.player(nickname)
    if user is not None:
        print(user)

    await obj.close()  # Closing client Not necessary
    assert isinstance(user, Player)


asyncio.run(main())
