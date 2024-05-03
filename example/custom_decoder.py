import asyncio
import orjson
from ddapi import DDnetApi, DDPlayer


async def main():
    obj = DDnetApi(json_loads=orjson.loads)  # json.loads
    nickname = "Cor"
    user: DDPlayer = await obj.player(nickname)
    if user is None:
        await obj.close()
        return "Player not found"
    print(f"{user.player}: {user.hours_played_past_365_days}")
    await obj.close()  # Closing client Not necessary
    assert isinstance(user, DDPlayer)


asyncio.run(main())
