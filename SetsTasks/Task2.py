"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]

mutable_elements = []

testSet = set(item if isinstance(item, (int, float, str, tuple)) else mutable_elements.append(item) for item in testList)

all_immutable = None not in testSet

print(all_immutable)
print(mutable_elements)

