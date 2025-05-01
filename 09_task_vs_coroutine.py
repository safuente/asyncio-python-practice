import asyncio
import time


# A simple coroutine that simulates some work with a delay
async def simple_coroutine(name, delay):
    print(f"{name}: started")              # Log when the coroutine starts
    await asyncio.sleep(delay)             # Simulate asynchronous delay
    print(f"{name}: finished after {delay}s")  # Log when it finishes
    return f"{name} result"                # Return a result string


# Main coroutine to demonstrate the difference between coroutine and task
async def main():
    start = time.perf_counter()            # Record the start time

    # Create a coroutine object — this does NOT start execution yet
    coro = simple_coroutine("CoroutineOnly", 2)

    # Create a task from the same coroutine — this schedules it immediately
    task = asyncio.create_task(simple_coroutine("Task", 2))

    print("Before awaiting both")          # Log before starting either

    # Await the coroutine — it starts executing here
    result1 = await coro

    # Await the task — it has already been running in the background
    result2 = await task

    print("After awaiting both")           # Log after both are completed
    print(f"Coroutine result: {result1}")  # Print result of coroutine
    print(f"Task result: {result2}")       # Print result of task

    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")  # Total duration

# Start the event loop and run the main coroutine
asyncio.run(main())
