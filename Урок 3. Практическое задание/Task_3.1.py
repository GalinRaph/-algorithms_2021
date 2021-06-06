from time import time

my_list = []
my_dict = {}

quantity = 10000000


def my_decorator(my_func):
    def timer(*args):
        first_time = time()
        result = my_func(*args)
        second_time = time()
        print(f'Время выполнения функции равно: {second_time - first_time}')
        return result

    return timer


@my_decorator
def insert_function(lst, value):
    for i in range(value):
        lst.insert(i, i)


"""Сложность операции O(n)"""

insert_function(my_list, quantity)

"""Время выполнения функции в первый раз равно: 1.5830566883087158"""
my_list = []


@my_decorator
def append_function(lst, value):
    for i in range(value):
        lst.append(i)
        """Сложность операции O(1) """


append_function(my_list, quantity)

"""Время выполнения функции в первый раз равно: 1.2348251342773438"""


@my_decorator
def dict_function(dct, value):
    for i in range(value):
        dct[i] = i


"""Сложность операции О(1)"""

dict_function(my_dict, quantity)

"""Время выполнения функции в первый раз равно: 1.2888634204864502"""


@my_decorator
def change_list(lst):
    for i in range(5000):
        lst.pop(i)
    for k in range(5000):
        lst[k] = '2'


change_list(my_list)
"""Время выполнения функции в первый раз равно: 48.256253719329834"""


@my_decorator
def change_dict(dct):
    for i in range(5000):
        dct.pop(i)
    for k in range(5000):
        dct[k] = '1'


change_dict(my_dict)

"""Время выполнения функции в первый раз равно: 0.004002571105957031"""

"""
В функции change_list(lst) операции удаления элемента не 
с конца списка lst.pop(i) выполняются за О(n). Обращение по
индексу с изменением элемента списка выполняется за О(1).
В функции change_dict(some_dict) все операции 
изменения словаря проходят за время O(1).
Следовательно функция по изменению словаря отрабатывает гораздо быстрее.
"""
