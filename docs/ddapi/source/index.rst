.. ddapi documentation master file, created by
   sphinx-quickstart on Tue May 14 11:28:57 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

What is ddapi used for?
=================================
   The ddapi tool is used to parsing or retrieving information from the DDraceNetwork game using the official api.


examples
=================================
I'll show you one example here

.. code-block:: python

   import asyncio
   from ddapi import DDnetApi, DDPlayer

   async def main():
       obj = DDnetApi()
       nickname = "Cor"
       user: DDPlayer = await obj.player(nickname)
       if user is None:
           await obj.close()
           return "Player not found"
       print(f"{user.player}: {user.points.total}")
       await obj.close()  # Closing client Not necessary
       assert isinstance(user, DDPlayer)


   asyncio.run(main())



.. _github: https://github.com/ByFox213/ddapi/tree/main/example

other examples on `github`_.
