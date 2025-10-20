import asyncio

ERROR_TEXT = 'Ошибка деления'
PAUSE_TIME = 0.1


async def safe_divide(a, b):
    await asyncio.sleep(PAUSE_TIME)
    try:
        return a / b
    except ZeroDivisionError:
        return ERROR_TEXT


async def run_divisions():
    attempts = [
        safe_divide(10, 2),
        safe_divide(10, 0),
        safe_divide(10, 5),
    ]
    results = await asyncio.gather(*attempts)
    return results
