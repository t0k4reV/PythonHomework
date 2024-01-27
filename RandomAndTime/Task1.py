"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""
from time import *

def timecount():
    return time() - startmove
print('Введите ход, например, E2-E4')
allmoves = []
move = (input())
allmoves.append(move)
game = True
start = time()
while game:
    startmove = time()
    move = input()
    allmoves.append(move)

    print("ход был сделан за: ",timecount())
    print('Осталось времени: ', (start+1800 - time())/60, ' минут')

    if move == 'off' or time() - start >= 1800:
        game = False
        print('Игро окончена')
        break
    print('Введите ход, например, E2-E4')
print(f'Список ходов: {allmoves}')






