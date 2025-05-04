import asyncio
import time


# Coroutine that runs a subprocess command asynchronously
async def run_subprocess():
    print("Running subprocess: 'ls -l' (or 'dir' on Windows)")

    # Launch an external subprocess using asyncio
    # Change to ["cmd", "/c", "dir"] if you're using Windows
    process = await asyncio.create_subprocess_exec(
        "ls", "-l",  # List directory contents
        stdout=asyncio.subprocess.PIPE,   # Capture standard output
        stderr=asyncio.subprocess.PIPE    # Capture standard error
    )

    # Wait for the subprocess to complete and gather its output
    stdout, stderr = await process.communicate()

    # Print the exit code of the subprocess
    print(f"\n[Exit code]: {process.returncode}")

    # Print the standard output if available
    if stdout:
        print("[STDOUT]:")
        print(stdout.decode())

    # Print the standard error if available
    if stderr:
        print("[STDERR]:")
        print(stderr.decode())


# Main coroutine to run the subprocess and measure execution time
async def main():
    start = time.perf_counter()       # Record the start time
    await run_subprocess()            # Run the subprocess coroutine
    duration = time.perf_counter() - start
    print(f"\nExecution time: {duration:.2f} seconds")  # Display total time taken

# Run the main coroutine inside the asyncio event loop
asyncio.run(main())
