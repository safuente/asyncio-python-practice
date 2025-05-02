import asyncio
import time


# Simple coroutine that simulates asynchronous work
async def say_hello():
    print("Hello from coroutine")      # Log message at start
    await asyncio.sleep(1)            # Simulate a 1-second non-blocking delay
    print("Goodbye from coroutine")    # Log message after delay

# Coroutine that prints the event loop's internal time
async def print_loop_time(loop):
    # Access and print the event loop's internal clock
    print(f"Loop time: {loop.time()} (event loop internal clock)")

# Synchronous function that sets up and manually runs the event loop
def main():
    start = time.perf_counter()        # Record the start time

    # Create a new event loop (instead of using asyncio.run)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)      # Set it as the current event loop

    try:
        # Run the say_hello coroutine until it completes
        loop.run_until_complete(say_hello())

        # Run the print_loop_time coroutine using the same loop
        loop.run_until_complete(print_loop_time(loop))
    finally:
        # Always close the event loop to clean up system resources
        loop.close()

    # Measure and print how long the program took
    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")

# Ensure main runs only if this script is executed directly
if __name__ == "__main__":
    main()
