from random import uniform
from timeit import timeit


def merge(left_lst, right_lst):
    """Выполняет слияние подсписков"""
    sorted_lst = []
    left_lst_index = right_lst_index = 0

    left_lst_length, right_lst_length = len(left_lst), len(right_lst)

    for _ in range(left_lst_length + right_lst_length):
        if left_lst_index < left_lst_length and \
                right_lst_index < right_lst_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше,
            # добавляем его в отсортированный массив
            if left_lst[left_lst_index] <= right_lst[right_lst_index]:
                sorted_lst.append(left_lst[left_lst_index])
                left_lst_index += 1
            # Если первый элемент правого подсписка меньше,
            # добавляем его в отсортированный массив
            else:
                sorted_lst.append(right_lst[right_lst_index])
                right_lst_index += 1

        # Если достигнут конец левого списка,
        # элементы правого списка добавляем в конец результирующего списка
        elif left_lst_index == left_lst_length:
            sorted_lst.append(right_lst[right_lst_index])
            right_lst_index += 1
        # Если достигнут конец правого списка,
        # элементы левого списка добавляем в отсортированный массив
        elif right_lst_index == right_lst_length:
            sorted_lst.append(left_lst[left_lst_index])
            left_lst_index += 1
    return sorted_lst


def merge_sort(nums):
    if len(nums) <= 1:  # Базовый случай
        return nums

    mid = len(nums) // 2  # Ищем середину списка

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


# сделаем замеры на массивах разной длины
lst_1 = [uniform(0, 50) for _ in range(100)]
print('Время выполнения merge_sort() при длине массива 100: ', timeit(
    'merge_sort(lst_1[:])',
    globals=globals(),
    number=100
))

print('-' * 160)
lst_2 = [uniform(0, 50) for _ in range(1000)]
print('Время выполнения merge_sort() при длине массива 1000: ', timeit(
    'merge_sort(lst_2[:])',
    globals=globals(),
    number=100
))

print('-' * 160)
lst_3 = [uniform(0, 50) for _ in range(10000)]
print('Время выполнения merge_sort() при длине массива 10000: ', timeit(
    'merge_sort(lst_3[:])',
    globals=globals(),
    number=100
))

print('-' * 160)
lst_4 = [uniform(0, 50) for _ in range(100000)]
print('Время выполнения merge_sort() при длине массива 100000: ', timeit(
    'merge_sort(lst_4[:])',
    globals=globals(),
    number=100
))
