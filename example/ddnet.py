import asyncio

from ddapi import DDnetApi, DDPlayer


async def main():
    obj = DDnetApi()
    nickname = "Cor"
    user: DDPlayer = await obj.player(nickname)
    if user is None:
        await obj.close()
        return "Player not found"
    print(f"{user.player}: {user.points.points} / {user.points.total}")
    await obj.close()  # Closing client Not necessary
    assert isinstance(user, DDPlayer)


asyncio.run(main())
