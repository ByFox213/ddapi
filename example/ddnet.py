import asyncio

from ddapi import DDnetApi, DDPlayer


async def main() -> None:
    async with DDnetApi() as obj:
        user: DDPlayer = await obj.player("Cor")
    if user is not None:
        text = f"{user.player}: {user.points.points}/{user.points.total}"
        percent = round(user.points.total / user.points.points * 100)
        print(f"{text}({percent}%)")
    else:
        print("Player not found")


asyncio.run(main())
