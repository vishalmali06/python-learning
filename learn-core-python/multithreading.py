import time
import threading


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {(end - start) * 1000:.2f} ms")
        return result
    return wrapper


def calc_square(numbers):
    print("Square calculation started")
    result = [n * n for n in range(numbers)]
    print("Square calculation finished")
    return result


def calc_cube(numbers):
    print("Cube calculation started")
    result = [n ** 3 for n in range(numbers)]
    print("Cube calculation finished")
    return result


@timeit
def run_with_threads(numbers):
    # Create threads
    t1 = threading.Thread(target=calc_square, args=(numbers,))
    t2 = threading.Thread(target=calc_cube, args=(numbers,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads to finish
    t1.join()
    t2.join()


# Parallel execution
run_with_threads(1_000_000)
