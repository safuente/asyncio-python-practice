import asyncio
import time


# Define an asynchronous function that simulates a slow task
async def slow_task(id):
    print(f"Task {id} started...")  # Indicate task start

    # Pause this coroutine for 2 seconds without blocking the event loop
    await asyncio.sleep(2)

    print(f"Task {id} finished.")  # Indicate task completion


# Define the main coroutine that coordinates all tasks
async def main():
    # Record the start time to measure total execution time
    start = time.perf_counter()

    # Create a list of 5 asynchronous tasks (from ID 0 to 4)
    # Each task runs concurrently thanks to asyncio.create_task
    tasks = [asyncio.create_task(slow_task(i)) for i in range(5)]

    # Wait for all tasks to complete concurrently
    await asyncio.gather(*tasks)

    # Calculate total duration
    duration = time.perf_counter() - start

    # Print how long all tasks took to complete
    print(f"Execution time: {duration:.2f} seconds")

# Start the asyncio event loop and run the main coroutine
asyncio.run(main())
