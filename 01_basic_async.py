import asyncio
import time


# Basic coroutine that prints a message, waits for 1 second, and prints again
async def say_hello():
    print("Hello")                  # Print first message
    await asyncio.sleep(1)         # Pause asynchronously for 1 second
    print("World")                 # Print second message after delay


# Main coroutine to run the say_hello coroutine and measure its duration
async def main():
    start = time.perf_counter()    # Record start time
    await say_hello()              # Call and await the coroutine
    duration = time.perf_counter() - start  # Calculate duration
    print(f"Execution time: {duration:.2f} seconds")  # Print total time taken

# Start the asyncio event loop and run the main coroutine
asyncio.run(main())
