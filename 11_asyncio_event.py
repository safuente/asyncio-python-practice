import asyncio
import time

# Shared asyncio Event — used for communication between coroutines
event = asyncio.Event()


# Coroutine that waits until the event is set
async def waiter(id):
    print(f"Waiter {id} is waiting for the event...")  # Log that this waiter is waiting
    await event.wait()                                # Suspend until the event is set
    print(f"Waiter {id} detected event set!")          # Continue once the event is triggered


# Coroutine that waits 3 seconds and then sets the event
async def set_event_later():
    print("Setter: sleeping for 3 seconds before setting the event.")  # Delay before setting the event
    await asyncio.sleep(3)            # Simulate delay
    event.set()                       # Signal all waiters — they can now continue
    print("Setter: event has been set!")  # Log that the event is set


# Main coroutine that orchestrates the waiters and setter
async def main():
    start = time.perf_counter()       # Record the start time

    # Create 3 waiter tasks that wait for the event
    waiters = [asyncio.create_task(waiter(i)) for i in range(3)]

    # Create one task to set the event after a delay
    setter = asyncio.create_task(set_event_later())

    # Wait for all tasks (waiters and setter) to finish
    await asyncio.gather(*waiters, setter)

    # Measure and print total time taken
    duration = time.perf_counter() - start
    print(f"Execution time: {duration:.2f} seconds")

# Start the asyncio event loop and run the main coroutine
asyncio.run(main())
