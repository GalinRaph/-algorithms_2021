
import collections
import functools


def calc():
    nums = collections.defaultdict(list)

    # defaultdict(<class 'list'>,
    # {'1-A2': ['A', '2'], '2-C4F': ['C', '4', 'F']})
    for d in range(2):
        n = input(f"Введите {d+1}-е натуральное шестнадцатиричное число: ")
        nums[f"{d+1}-{n}"] = list(n)
    print(nums)

    # 16-указываем с числами какой системы делаем операции
    sum_res = sum([int(''.join(i), 16) for i in nums.values()])
    print(sum_res)
    # '%X'	Число в шестнадцатеричной системе счисления

    print("Сумма: ", list('%X' % sum_res))
    # f'{15:x}' -> f
    mul_res = functools.reduce(lambda a, b: a * b,
                               [int(''.join(i), 16) for i in nums.values()])
    print("Произведение: ", list('%X' % mul_res))


calc()
