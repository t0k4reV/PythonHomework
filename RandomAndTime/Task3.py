"""
На летней универсиаде будет проводиться по два забега. Чтобы соревнования были честными,
участники должны распределяться между забегами случайным образом.
Напишите программу, печатающую случайные номера забегов (1 или 2) до тех пор, пока не будет введено «off».
После генерации каждого номера должно печататься:
1) «Ваш номер: _».
2) «Участников в первом забеге: _», «Участников во втором забеге: _».
"""
from random import choice

first = {}
second = {}
i = 0
inp = input("Enter your fullname: ")

while inp != 'off':
    run = choice([1,2])
    if run == 1:
        first[i] = inp
    else:
        second[i] = inp

    print(f"{inp} your number is {i}")

    print(f" Number of participants in first race: {len(first)}")
    print(f"Number of participants in second race: {len(second)}")

    inp = input("Enter your fullname: ")
    i += 1

print(first)
print(second)

