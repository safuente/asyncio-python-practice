import asyncio
import time

# Semaphore to limit concurrent tasks
semaphore = asyncio.Semaphore(3)


# Simulated async task with access control via semaphore
async def limited_task(id):
    async with semaphore:
        print(f"Task {id} started")
        await asyncio.sleep(2)
        print(f"Task {id} finished")


async def main():
    start = time.perf_counter()

    # Launch 10 tasks but only 3 will run at the same time
    tasks = [asyncio.create_task(limited_task(i)) for i in range(10)]

    await asyncio.gather(*tasks)

    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")


asyncio.run(main())
