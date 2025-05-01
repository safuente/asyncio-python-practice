import asyncio
import time


# Coroutine that waits for a Future to be resolved
async def waiter(future):
    print("Waiting for future result...")
    result = await future             # Suspend here until the future is resolved
    print(f"Future completed with result: {result}")


# Coroutine that resolves the Future after a delay
async def resolver(future):
    print("Resolver sleeping for 2 seconds...")
    await asyncio.sleep(2)            # Simulate delay before resolving
    future.set_result("Task completed!")  # Set the result of the future
    print("Resolver has set the future result.")


# Main coroutine to coordinate the process
async def main():
    start = time.perf_counter()       # Start timer

    # Get the current event loop and manually create a Future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()     # Future starts unresolved

    # Run both coroutines concurrently: one waits, the other resolves
    await asyncio.gather(
        waiter(future),
        resolver(future)
    )

    # Measure and print total execution time
    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")

# Start the asyncio event loop and run the main coroutine
asyncio.run(main())
