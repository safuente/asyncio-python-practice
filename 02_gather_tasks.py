import asyncio
import time


# Coroutine that simulates a greeting delay
async def greet(name):
    print(f"Greeting {name}")
    await asyncio.sleep(1)
    print(f"Hello {name}!")


async def main():
    start = time.perf_counter()
    # Run all greetings concurrently in 1 second
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    )
    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")

asyncio.run(main())
