"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""
from random import randint
from time import sleep

def dice():
    print('tossing the dice')
    sleep(2)
    print(randint(1,6), randint(1,6))

dice()