"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""


def diploma(s):
    if s > 80:
        return "diploma"
    elif 50 < s <= 80:
        return "certificate of commendation"
    else:
        return "certificate of participation"


name = input("Enter your name: ")
while name != 'stop':
    subjects = int(input('how many subject do you have?'))
    s = 0
    for i in range(subjects):
        n = int(input(f'enter the score for subject {i + 1}: '))
        s += n
    print(diploma(s))

    name = input("Enter your name: ")

