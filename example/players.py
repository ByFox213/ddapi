import asyncio

from ddapi import DDnetApi, DDPlayer


async def main():
    obj = DDnetApi()
    nicknames = ["Cor", "ByFox"]
    users: tuple[DDPlayer] = await obj.players(nicknames)
    for user in users:
        if user is None:
            await obj.close()
            return f"Player \"{user}\" not found"
        print(f"{user.player}: {user.points.points} / {user.points.total}")
    await obj.close()  # Closing client Not necessary
    assert isinstance(users, list)


asyncio.run(main())
