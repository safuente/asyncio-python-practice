import asyncio
import time

# Coroutine that performs a periodic task at a given interval
async def periodic(name, interval, stop_after=5):
    count = 0
    print(f"[{name}] Starting periodic task every {interval}s...")

    # Run the loop until the specified number of ticks
    while count < stop_after:
        print(f"[{name}] Tick {count + 1}")     # Log the current tick
        await asyncio.sleep(interval)           # Wait for the specified interval (non-blocking)
        count += 1

    print(f"[{name}] Done!")                    # Task complete after stop_after ticks

# Main coroutine to launch and run multiple periodic tasks concurrently
async def main():
    start = time.perf_counter()  # Record start time

    # Run two periodic coroutines concurrently:
    # - TimerA ticks every 1 second, 3 times
    # - TimerB ticks every 0.5 seconds, 5 times
    await asyncio.gather(
        periodic("TimerA", 1, stop_after=3),
        periodic("TimerB", 0.5, stop_after=5)
    )

    # Measure and print total execution time
    duration = time.perf_counter() - start
    print(f"\nExecution time: {duration:.2f} seconds")

# Start the event loop and run the main coroutine
asyncio.run(main())
