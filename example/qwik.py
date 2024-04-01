import asyncio
from ddapi import Player, DDraceAPI


async def main():
    obj = DDraceAPI()
    nickname = "ByFox"
    user = await obj.player(nickname)
    if user is None:
        return "Player not found"
    print(user)
    await obj.close()  # Closing client Not necessary
    assert isinstance(user, Player)


asyncio.run(main())
