import time


def timeit(func):
    """
    Decorator to measure execution time of a function
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()   # High-precision timer
        result = func(*args, **kwargs)
        end = time.perf_counter()

        execution_time = (end - start) * 1000  # Convert to milliseconds
        print(f"{func.__name__} took {execution_time:.2f} ms")

        return result

    return wrapper


@timeit
def calc_square(numbers):
    """
    Calculates square of numbers from 0 to numbers-1
    """
    result = []
    for number in range(numbers):
        result.append(number * number)
    return result


@timeit
def calc_cube(numbers):
    """
    Calculates cube of numbers from 0 to numbers-1
    """
    result = []
    for number in range(numbers):
        result.append(number * number * number)
    return result


# Function calls
calc_square(1000)
calc_cube(1000)
