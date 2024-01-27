arr = []
game = input('введите игру ')
while game != '0':
    if game in arr:
        print('Игра уже есть в списке')
    else:
        arr.append(game)
    game = input('введите игру ')
arr.sort()
print(arr)
