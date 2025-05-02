import asyncio
import time
import traceback


# A coroutine that simulates work and raises an error if input is 0
async def faulty_coroutine(x):
    print(f"Running faulty_coroutine({x})")
    await asyncio.sleep(1)  # Simulate async delay
    if x == 0:
        # Raise an exception if x is zero
        raise ValueError("Division by zero is not allowed.")
    return 10 / x           # Return division result if x != 0


# Main coroutine to handle errors from the async task
async def main():
    start = time.perf_counter()  # Start timing execution

    try:
        # Await the coroutine — this will raise an exception if x == 0
        result = await faulty_coroutine(0)
        print(f"Result: {result}")  # This line won't be reached if an error occurs
    except Exception as e:
        # Handle and report any exception raised inside the coroutine
        print("An error occurred inside the coroutine!")
        traceback.print_exc()  # Print full traceback for debugging

    # Print total execution time
    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")

# Start the event loop and run the main coroutine
asyncio.run(main())
