import asyncio  # For asynchronous programming
import time  # For measuring execution time


# Asynchronous function that simulates a slow, long-running operation
async def slow_task():
    print("Slow task starting...")
    await asyncio.sleep(5)  # Simulate a delay of 5 seconds
    print("Slow task completed.")


# Main coroutine that controls the timeout behavior
async def main():
    start = time.perf_counter()  # Record the start time for performance measurement
    try:
        # Run the slow_task but enforce a timeout of 2 seconds
        # If slow_task takes longer than 2 seconds, it will raise a TimeoutError
        await asyncio.wait_for(slow_task(), timeout=2)
    except asyncio.TimeoutError:
        # Handle the case where the task took too long
        print("Task timed out!")

    # Calculate how long the operation took (should be close to 2 seconds)
    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")


# Launch the main coroutine inside the asyncio event loop
asyncio.run(main())
