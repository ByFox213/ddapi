ddapi is an api from the ddnet and qwik website
## Installation

```bash
  pip install ddapi
```
or
```bash
  pip install git+https://github.com/ByFox213/ddapi
```
    
## Usage/Examples

DDnet
```python
import asyncio
from ddapi import DDnetApi, DDPlayer


async def main():
    obj = DDnetApi()
    nickname = "Cor"
    user: DDPlayer = await obj.player(nickname)
    if user is None:
        return "Player not found"
    print(f"{user.player}: {user.points.points}")
    # Cor: 31473 
    await obj.close()  # Closing client Not necessary
    assert isinstance(user, DDPlayer)


asyncio.run(main())
```

qwik

```python
import asyncio
from ddapi import Player, QwikAPI


async def main():
    obj = QwikAPI()
    nickname = "ByFox"
    user = await obj.player(nickname)
    if user is None:
        return "Player not found"
    print(f"{user.player}: {user.points.points}")
    # Cor: 31473 
    await obj.close()  # Closing client Not necessary
    assert isinstance(user, Player)


asyncio.run(main())
```
