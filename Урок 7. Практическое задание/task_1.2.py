

import random
import timeit


def bubble_sort_unoptimized(some_lst):
    """Выполняет самую простую сортировку пузырьком"""
    for i in range(len(some_lst)):
        for j in range(len(some_lst) - 1):
            if some_lst[j] < some_lst[j + 1]:
                some_lst[j], some_lst[j + 1] = some_lst[j + 1], some_lst[j]
    return some_lst


def bubble_sort_optimized1(some_lst):
    """Сортировка пузырьком с использованием маркера"""
    flag = True
    while flag:
        flag = False
        for i in range(len(some_lst) - 1):
            if some_lst[i] < some_lst[i + 1]:
                some_lst[i], some_lst[i + 1] = some_lst[i + 1], some_lst[i]
                flag = True
    return some_lst


orig_list = [random.randint(-100, 100) for i in range(1000)]

print(
    timeit.timeit(
        "bubble_sort_unoptimized(orig_list[:])",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "bubble_sort_optimized1(orig_list[:])",
        globals=globals(),
        number=100))

# результат
"""
17.006069507000003
17.099994868000003
"""
