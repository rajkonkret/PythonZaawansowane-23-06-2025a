import concurrent.futures
import time


def long_task(name, duration):
    print(f"Task {name} starting")
    time.sleep(duration)
    print(f"Task {name} completed after {duration} second")


def main():
    tasks = [
        ('A', 2),
        ('B', 1),
        ('C', 3),
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(long_task, name, duration): name for name, duration in tasks}
        for future in concurrent.futures.as_completed(futures):
            future.result()

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     futures = {executor.submit(long_task, name, duration): name for name, duration in tasks}
    #     for future in concurrent.futures.as_completed(futures):
    #         future.result()


# start_time = time.time()
# main()
# end_time = time.time()
# print(f"Total time: {end_time - start_time}")

# wymagane dla ProcessPoolExecutor()
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total time: {end_time - start_time}")
