import timeit


def func_1(nums):
    """O(n) – линейная сложность"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# lc - list comprehension
def func_2(nums):
    """O(n) – линейная сложность"""
    return [i for i, el in enumerate(nums) if el % 2 == 0]


# 1000
NUMS = [el for el in range(1000)]

print(
    timeit.timeit(
        "func_1(NUMS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(NUMS)",
        globals=globals(),
        number=1000))


# 10000
NUMS = [el for el in range(10000)]

print(
    timeit.timeit(
        "func_1(NUMS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(NUMS)",
        globals=globals(),
        number=1000))

# 100000
NUMS = [el for el in range(100000)]

print(
    timeit.timeit(
        "func_1(NUMS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(NUMS)",
        globals=globals(),
        number=1000))

"""
Результат:
---1000---
0.11944510000000001
0.09699780000000002

---10000---
0.9557013000000001
0.7219996999999998

---100000---
10.0411876
7.4286987

Списковые включения отрабатывают быстрее, чем привычная реализация итераторов
"""
