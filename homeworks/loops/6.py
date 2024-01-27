price = int(input())
res = 0
while price != 0:
    res += price
    price = int(input())

if res%2 == 0:
    while res%2==0:
        res /= 2
    print(f'the result is {res}')
else:
    print(f'the result is {res*0.85}')

