"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
dict = {'1': ' value1',
              '2': 'value2',
              '3': 'value3',
              '4': 'value4',
              '5': 'value5'}

#Создаем второй словарь, чтобы добавить объект 5 и его значение в начало словаря 1
dict2 = {'5': 'value5'}

#Удаляем наш первый элемент в словаре 1
del dict['1']

#Меняем местами словарь 1 и словарь 2
dict, dict2 = dict2, dict

#Из-за перестановки теперь мы можем добавить словарь 2 в начало словаря 1
dict.update(dict2)

#Добавляем объект 1 в конец словаря
dict['1'] = 'value1'

#По заданию удаляем второй элемент в словаре 1 и добавляем новую пару ключ-значение в конец
del dict['2']
dict['new'] = 'new value'

print(dict)