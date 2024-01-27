FullName = input('Введите полное имя: ')
line = list(FullName.split(" "))
Surname = line[0]
Name = line[1][: 1] + '.'
FatherName = line[2][: 1] + '.'
ShortName = Surname + ' ' + Name + FatherName
print(ShortName)
