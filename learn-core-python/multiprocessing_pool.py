from multiprocessing import Pool
import time


def f(_):
    total = 0
    for x in range(1000):
        total += x * x
    return total


if __name__ == '__main__':
    t1 = time.time()

    with Pool(processes=4) as p:
        result = p.map(f, range(1_000_000), chunksize=1000)

    print("Pool took", time.time() - t1)

    t2 = time.time()
    result = [f(x) for x in range(1_000_000)]
    print("Serial took", time.time() - t2)
