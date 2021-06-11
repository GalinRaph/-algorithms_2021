from collections import deque
from timeit import timeit
from random import randint

n = 10 ** 4
some_lst1 = []  # инициализируем для тестирования скорости заполнения
some_deque1 = deque()  # инициализируем для тестирования скорости заполнения
some_lst2 = [i for i in range(10 ** 5)]  # заполняем заранее, чтобы не
                                        # отражалось на замерах при изменении
some_deque2 = deque([i for i in range(10 ** 5)])  # заполняем заранее,
                                # чтобы не отражалось на замерах при изменении


def fill_list(lst):
    """Заполняет пустой список, вставляя элементы в его начало"""
    for i in range(n):
        lst.insert(0, i)
    return lst


def fill_deque(dq):
    """Заполняет пустую двустороннюю очередь"""
    for i in range(n):
        dq.appendleft(i)
    return dq


def change_list(lst):
    """Изменяет 90000 случайных элементов
    заранее заполненного списка"""
    for _ in range(90000):
        lst[randint(1, 8001)] = randint(1, 150)
    return lst


def change_deque(dq):
    """Изменяет 90000 случайных элементов
    заранее заполненной двусторонней очереди"""
    for _ in range(90000):
        dq[randint(1, 8001)] = randint(1, 150)
    return dq


if __name__ == '__main__':
    print('Время заполнения списка при 10 повторениях: ', timeit(
        'fill_list(some_lst1)',
        setup='from __main__ import fill_list, some_lst1, n',
        number=10
    ))

    print('Время заполнения двусторонней очереди при 10 повторениях: ', timeit(
        'fill_deque(some_deque1)',
        setup='from __main__ import fill_deque, some_deque1, n',
        number=10
    ))
    """
    Если заполнение списка проиходит путем вставки элемента в начало списка, 
    то двусторонняя очередь работает гораздо
    быстрее, чем обычный список, так как сложность операции вставки в начало 
    и конец для нее О(1), для списка же
    сложность операции вставки в начало - О(n).
    Если заполнять списки путем добавления элементов в конец списка, 
    то время работы сопоставимо, так как сложность
    операции составляет О(1) и в том и другом случае. Дек заполняется 
    чуть быстрее при большом количестве элементов.
    """

    print('-' * 150)
    print('Время изменения списка при 10 повторениях: ', timeit(
        'change_list(some_lst2)',
        setup='from __main__ import change_list, some_lst2',
        number=10
    ))
    print('Время изменения двусторонней очереди при 10 повторениях: ', timeit(
        'change_deque(some_deque2)',
        setup='from __main__ import change_deque, some_deque2',
        number=10
    ))
    """
    При случайном доступе к элементу по индексу и изменении элемента,
    обычный список работает быстрее, чем дек.
    """
