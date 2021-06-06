import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} seconds...")
    time.sleep(seconds)
    return "Done sleeping!"


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)
#     print(f1.result())
#     print(f2.result())

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(do_something, secs) for secs in range(1, 6)]
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [i for i in range(1, 6)]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds")