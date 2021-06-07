import multiprocessing
import time


def do_something(seconds):
    print(f"Sleeping {seconds} seconds...")
    time.sleep(seconds)
    print("Done sleeping...")


if __name__ == '__main__':
    start = time.perf_counter()

    # p1 = multiprocessing.Process(target=do_something, args=[1])
    # p2 = multiprocessing.Process(target=do_something, args=[1])
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} seconds")