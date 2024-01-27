"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""


def calculate(*n):
    ft = list()
    numlist = list()
    avgn = sum(n) / len(n)
    ft.append(round(avgn, 2))
    for i in n:
        if i > avgn:
            numlist.append(i)
    ft.append(numlist)
    print(tuple(ft))


calculate(*[int(x) for x in input('Enter the numbers: ').split(' ')])
