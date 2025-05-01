import asyncio
import time

counter = 0  # Shared global counter
lock = asyncio.Lock()  # Asynchronous lock to ensure safe access to shared data


# Coroutine that safely increments the global counter
async def increment():
    global counter
    # Acquire the lock before modifying the counter (to avoid race conditions)
    async with lock:
        temp = counter              # Read the current value
        await asyncio.sleep(0.1)    # Simulate a delay (could cause race condition without lock)
        counter = temp + 1          # Safely update the shared counter


# Main coroutine that launches many concurrent increment operations
async def main():
    start = time.perf_counter()  # Record start time for performance measurement

    # Create 10 increment tasks (to run concurrently)
    tasks = [increment() for _ in range(10)]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    # Measure total time taken
    duration = time.perf_counter() - start

    # Print final result and execution time
    print(f"Final counter value: {counter}")
    print(f"Execution time: {duration:.2f} seconds")

# Start the asyncio event loop and run the main coroutine
asyncio.run(main())
