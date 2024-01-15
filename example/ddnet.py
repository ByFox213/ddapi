import asyncio

from DDnetApiPy import DDnetApi
from dataclass import DDPlayer


async def main():
    obj = DDnetApi()
    nickname = "Cor"
    user: DDPlayer = await obj.player(nickname)
    if user is None:
        return "Player not found"
    print(f"{user.player}: {user.points.points}")
    await obj.close()  # Closing client Not necessary
    assert isinstance(user, DDPlayer)


asyncio.run(main())
