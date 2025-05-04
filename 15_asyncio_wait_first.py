import asyncio
import time


# Simulated asynchronous task with a variable delay
async def task(name, delay):
    print(f"{name} started, will finish in {delay} seconds")  # Log start
    await asyncio.sleep(delay)                                # Simulate delay
    print(f"{name} finished")                                 # Log completion
    return f"{name} result"                                   # Return task result


# Main coroutine to manage multiple tasks and handle early completion
async def main():
    start = time.perf_counter()  # Record start time

    # Create three tasks with different durations using create_task
    t1 = asyncio.create_task(task("TaskA", 3))
    t2 = asyncio.create_task(task("TaskB", 1))
    t3 = asyncio.create_task(task("TaskC", 2))

    # Wait until the first task finishes (others may still be running)
    done, pending = await asyncio.wait(
        [t1, t2, t3],
        return_when=asyncio.FIRST_COMPLETED  # Return as soon as one finishes
    )

    # Print the result of the completed task(s)
    for d in done:
        print(f"First completed result: {await d}")

    # Cancel any remaining tasks that are still pending
    for p in pending:
        print(f"Cancelling {p.get_name()}")  # Note: get_name() may require Python 3.8+
        p.cancel()                             # Cancel the task

    # Calculate and display total execution time
    duration = time.perf_counter() - start
    print(f"\nExecution time: {duration:.2f} seconds")

# Start the event loop and run the main coroutine
asyncio.run(main())
