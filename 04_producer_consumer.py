import asyncio
import time


# Asynchronous producer coroutine that adds items to the queue
async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)            # Simulate some delay in producing items
        print(f"Producing {i}")           # Log the produced item
        await queue.put(i)                # Put the item into the queue


# Asynchronous consumer coroutine that retrieves items from the queue
async def consumer(queue):
    while True:                           # Infinite loop to keep consuming
        item = await queue.get()          # Wait for an item to be available
        print(f"Consuming {item}")        # Log the consumed item
        queue.task_done()                 # Mark the item as processed


# Main coroutine to coordinate producer and consumer
async def main():
    start = time.perf_counter()          # Record the start time
    queue = asyncio.Queue()              # Create an asyncio queue for communication

    # Create and schedule the producer and consumer tasks
    prod = asyncio.create_task(producer(queue))
    cons = asyncio.create_task(consumer(queue))

    await prod                           # Wait for the producer to finish producing
    await queue.join()                   # Wait until the queue is fully processed

    cons.cancel()                        # Cancel the consumer task (infinite loop)
    duration = time.perf_counter() - start  # Calculate total execution time
    print(f"Execution time: {duration:.2f} seconds")

# Run the main coroutine in the event loop
asyncio.run(main())
