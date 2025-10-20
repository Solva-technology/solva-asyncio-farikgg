import asyncio

PAUSE_TIME = 0.1
SEMAPHORE_LIMIT = 2
AMOUNT_OF_TASKS = 5


async def limited_worker(task_id, semaphore):
    async with semaphore:
        await asyncio.sleep(PAUSE_TIME)
        return task_id


async def limited_runner():
    semaphore = asyncio.Semaphore(SEMAPHORE_LIMIT)
    tasks = [
        asyncio.create_task(limited_worker(i, semaphore))
        for i in range(AMOUNT_OF_TASKS)
    ]
    results = await asyncio.gather(*tasks)
    return results
