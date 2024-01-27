informationList = []
while True:
    personalInformation = []
    personalInformation.append(input('Введите фамилию: '))
    personalInformation.append(input('Должность:  '))
    numberOfStudents = [int(a) for a in input('Введите количество студентов во всех группах ').split()]
    personalInformation.append(numberOfStudents)
    informationList.extend(personalInformation)
    print('Хотите ли вы продолжить? (да или нет)')
    choose = input()
    if choose.lower() == 'да':
        continue
    else:
        break
print(informationList)


