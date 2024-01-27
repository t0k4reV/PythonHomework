"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""

def bmi(height,weight):
    return weight / ((height/100) ** 2)

def decode_bmi(height,weight):
    if bmi(height, weight) <= 18.5:
        return 'underweight', bmi(height, weight)
    elif bmi(height, weight) >= 25:
        return 'overweight', bmi(height, weight)
    else:
        return 'normal', bmi(height, weight)


print(decode_bmi(180, 90))

