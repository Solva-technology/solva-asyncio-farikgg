import asyncio

ASYNC_SLEEP_TIME = 1


async def delayed_echo(text: str, delay: int):
    await asyncio.sleep(delay)
    return text


async def echo_all():
    tasks = [
        delayed_echo("hello", ASYNC_SLEEP_TIME),
        delayed_echo("world", ASYNC_SLEEP_TIME),
        delayed_echo("!", ASYNC_SLEEP_TIME)
    ]
    results = await asyncio.gather(*tasks)
    return results
