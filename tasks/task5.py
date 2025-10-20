import asyncio

FAST_TIME = 0.1
MEDIUM_TIME = 0.3
SLOW_TIME = 1

RESULT_FAST_TASK = 'fast'
RESULT_MEDIUM_TASK = 'medium'
RESULT_SLOW_TASK = 'slow'


async def fast_task():
    await asyncio.sleep(FAST_TIME)
    return RESULT_FAST_TASK


async def medium_task():
    await asyncio.sleep(MEDIUM_TIME)
    return RESULT_MEDIUM_TASK


async def slow_task():
    await asyncio.sleep(SLOW_TIME)
    return RESULT_SLOW_TASK


async def first_complete():
    tasks = [
        asyncio.create_task(fast_task()),
        asyncio.create_task(medium_task()),
        asyncio.create_task(slow_task())
    ]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    first_result = next(iter(done)).result()

    for task in pending:
        task.cancel()

    return first_result
