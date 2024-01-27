"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def task1(f=None, s=None, t=None):
    if f: return 'first', f
    if s: return 'second', s
    if t: return 'third', t
    return None

print(task1(None, None, 'hello'))
