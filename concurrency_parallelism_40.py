from threading import Thread, Lock
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


# def task(x, lock):
#     # time.sleep(5)
#     with lock:
#         print(f"Thread executed. value {x}")

# thread = Thread(target=task, args=(9,))
# print(thread.is_alive())
# thread.start()
# print(thread.is_alive())
# thread.join()
# print(thread.is_alive())
# print("Waiting for the thread")

# threads = []
# lock = Lock()
# for x in range(5):
#     t = Thread(target=task, args=(x,lock))
#     threads.append(t)
#     t.start()

# for each in threads:
#     each.join()


# def task(x):
#     #print(f"Thread executed. value {x}")
#     return x
#                         # ThreadPoolExecutor
# items = [1, 2]                    
# with ThreadPoolExecutor(max_workers=2) as executor:
#     results = executor.map(task, items)
    
#     for result in results:
#         print(result)

# with ThreadPoolExecutor(max_workers=2) as executor:
#     future = executor.submit(task,1)
#     result = future.result()
#     print(result)
                        # Multiprocessing
# def task(x):
#     print(f"Process executed. value {x}")
#     return x              

# process = Process(target=task, args=(1,))
# process.start()
# process.join()

# for x in range(4):
#     p = Process(target=task, args=(x,))
#     p.start()

# with ProcessPoolExecutor(max_workers=2) as executor:
#     results = executor.map(task, (1, 2))

#     for result in results:
#         print(result)

                        # Asynchronous Programming 
import asyncio

async def read_data():
    # data = await db.fetch('SELECT ...')
    print("Coroutine was executed")
    return 5

result = asyncio.run(read_data())
print("result", result)

