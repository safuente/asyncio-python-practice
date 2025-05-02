# 🌀 Python Asyncio Examples

This repository contains a series of examples using Python's `asyncio` library. Each script is focused on a specific concept, with clear code and detailed comments in English.

> ✅ Ideal for learning asynchronous programming in Python with examples.

---

## 📚 Contents

| #  | Filename                  | Concept                                |
|----|---------------------------|----------------------------------------|
| 01 | `01_basic_async.py`       | Basic `async` / `await` usage          |
| 02 | `02_gather_tasks.py`      | Concurrent tasks with `asyncio.gather`|
| 03 | `03_create_tasks.py`      | Task management with `create_task`     |
| 04 | `04_producer_consumer.py` | Producer/Consumer with `Queue`         |
| 05 | `05_timeout.py`           | Task timeouts with `wait_for`          |
| 06 | `06_lock_counter.py`      | Synchronization with `Lock`            |
| 07 | `07_semaphore_limit.py`   | Limiting concurrency with `Semaphore`  |
| 08 | `08_future_manual.py`     | Manual `Future` object usage           |
| 09 | `09_task_vs_coroutine.py` | Difference between coroutine and task  |
| 10 | `10_debug_coroutine_error.py` | How to debug errors inside a coroutine |
| 11 | `11_asyncio_event.py`        | Coordination between tasks using `asyncio.Event` |


---

## 🛠️ Setup: Create a Virtual Environment with Python 3.11

Make sure you have **Python 3.11** installed on your system. Then follow these steps:

```bash
# Create a virtual environment using Python 3.11
python3.11 -m venv venv

# Activate the virtual environment
source venv/bin/activate      # On Windows: venv\Scripts\activate

# No external dependencies are required for these examples
# You're ready to run the examples:
python 01_basic_async.py

