"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
composotions = {}

chart = input("Enter the chart position: ")
while chart != 'off':
    key = ''
    permormer = input('Enter the performer: ')
    key = chart + ', ' + permormer
    song = input('Enter the song: ')
    composotions[key] = song
    chart = input('Enter the chart position: ')
print(composotions)



