"""
Во время хоккейных матчей на игроков может накладываться дисциплинарный штраф — удаление с поля на 2 или 10 минут.

Программа должна:
1) Спрашивать «Удалить с поля?» и запрашивать количество минут штрафа.
2) Печатать сообщение: «Вы удалена с поля на _ минут(-ы)» и ставить паузу в работе на это время.
3) Спустя 2 или 10 минут печатать новое сообщение: «Возвращайтесь на поле!»
Дабы не ждать 2 и 10 минут сделайте 2 и 10 секунд.
"""
from time import *

deleteornot = input("Delete from the field? (yes on no)?  ")

if deleteornot.lower() == 'yes':
    penaltytime = int(input("2 or 10 minutes  "))
    if penaltytime != 2 and penaltytime != 10:
        print('time is not correct')
    else:
        print(f'you have been deleted for {penaltytime} minutes')
        if penaltytime == 10:
            sleep(10)
        if penaltytime == 2:
            sleep(2)

        print("go back to the field")
