import asyncio
import time


# Basic coroutine that prints a message, waits, and prints again
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def main():
    start = time.perf_counter()
    await say_hello()
    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")

asyncio.run(main())
