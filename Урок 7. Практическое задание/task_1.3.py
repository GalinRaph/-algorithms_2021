

import random
import timeit


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


"""
Оптимизация заключается в виде сокращения диапазона внутреннего цикла 
в зависимости от итерации внешнего цикла.
Нет необходимости проходить внутренним циклом весь массив, 
так как с каждой итерацией растет число элементов,
которые уже стоят на своих местах.
"""


def bubble_sort_optimized2(some_lst):
    """Сортировка пузырьком с использованием маркера
    и сокращением числа итераций"""
    flag = True
    iter_counter = 0  # счетчик итераций
    while flag:
        flag = False
        # уменьшаем число итераций на 1 каждый раз
        for i in range(len(some_lst) - iter_counter - 1):
            if some_lst[i] < some_lst[i + 1]:
                some_lst[i], some_lst[i + 1] = some_lst[i + 1], some_lst[i]
                flag = True
        iter_counter += 1
    return some_lst


orig_list = [random.randint(-100, 100) for i in range(1000)]

print(
    timeit.timeit(
        "bubble_sort_optimized1(orig_list[:])",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "bubble_sort_optimized2(orig_list[:])",
        globals=globals(),
        number=100))

# результат
"""
16.483835378
11.067420513000002
"""
