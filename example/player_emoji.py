import asyncio
from ddapi import DDnetApi, DDPlayer


async def main():
    obj = DDnetApi()
    nickname = "ByFox"
    user: DDPlayer = await obj.player(nickname)
    if user is None:
        await obj.close()
        return "Player not found"
    print(f"{user.player}: {user.points.total} | {user.emoji}")
    await obj.close()  # Closing client Not necessary


asyncio.run(main())
