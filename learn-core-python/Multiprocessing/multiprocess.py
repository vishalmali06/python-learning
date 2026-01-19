import time
import multiprocessing


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
    time.sleep(1)
    result = [n * n for n in numbers]
    print("Square calculation finished")
    return result


def calc_cube(numbers):
    print("Cube calculation started")
    time.sleep(1)
    result = [n ** 3 for n in numbers]
    print("Cube calculation finished")
    return result


@timeit
def run_with_processes(numbers_list):
    p1 = multiprocessing.Process(target=calc_square, args=(numbers_list,))
    p2 = multiprocessing.Process(target=calc_cube, args=(numbers_list,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    run_with_processes([2, 3, 4, 5, 6, 7])
