import aiohttp

session = aiohttp.ClientSession()


async def close_session():
    await session.close()
