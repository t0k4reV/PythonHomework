"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""


def colors(num, **colors):
    print(f"Number of colors: {num}")
    for color, hex_color in colors.items():
        print(f'{color}: {hex_color}')


colors(3, LitePink='ffc0cb', Yellow='ffff00', Red='ff0000')
