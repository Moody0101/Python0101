from timeit import timeit

v = [
    2, 5, 4, 4, 7, 0, 8, 6
]
v.sort()


def bin(array: list, x) -> int:
    lo = 0
    hi = len(array)
    while lo < hi:
        middle = (lo + hi) // 2
        if array[middle] < x:
            lo = middle + 1
        else:
            hi = middle
    return lo


def find(x=100, n=100_001):
    """
    jgjg
    """
    arr = []
    for i in range(n):
        if i == 0:
            pass
        else:
            arr.append(i)
    return bin(arr, x)


def findinList(arr, x):
    if x in arr:
        return arr.index(x)
    else:
        return False


def list():
    i = [i for i in range(0, 100_000)]


def makelist():
    arr = [i for i in range(0, 100_000_0)]


if __name__ == '__main__':
    print('list ==> \t\t', timeit(list, number=1))
