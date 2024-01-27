"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""

n = int(input("Всего учеников:  "))
langall = list()

for i in range(n):
    while n != 0:
        lang = set()
        for _ in range(ngroup := int(input('количество учеников в группе:  '))):
            lang.add(input('Введите язык:  '))
            n -= 1

        langall.append(lang)

inter = langall[0]
union = langall[0]

for i in range(len(langall)):
    inter = inter & set(langall[i])
    union = union | set(langall[i])

print(f"Языки, которые знают все школьники -- {inter}")
print(f"Языки, которые знает хотя бы 1 школьник -- {union}")
