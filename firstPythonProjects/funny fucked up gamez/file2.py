from timeit import timeit


def makearray(n: list):
    x = []
    for i in n:
        if i % 2 == 0:
            x.append(n)
        else:
            pass
    print(x)


def makearray2(n: list):
    print([i for i in n if i % 2 == 0])




def iteration():
    makearray([i for i in range(0, 100_000)])


def comprehension():
    makearray2([i for i in range(0, 100_000)])


print("iteration\t", "==>\t", timeit(iteration, number=10))
print("comprehension\t", "==>\t", timeit(comprehension, number=10))
