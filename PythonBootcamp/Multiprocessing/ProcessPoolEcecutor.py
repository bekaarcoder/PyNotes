import concurrent.futures
import time


def do_something(seconds):
    print(f"Sleeping {seconds} seconds...")
    time.sleep(seconds)
    return f"Done sleeping for {seconds} seconds."


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # p1 = executor.submit(do_something, 1)
        # p2 = executor.submit(do_something, 1)
        # print(p1.result())
        # print(p2.result())

        # results = [executor.submit(do_something, secs) for secs in range(1, 5)]
        #
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        secs = [x for x in range(1, 6)]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} seconds")