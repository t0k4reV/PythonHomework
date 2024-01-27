discount = 15
price = int(input('введите стоимость '))
while price > 0:
    print(f"ваша цена с учетом скидки составляет: {(price * (100-discount))/100}")
    price = int(input('введите стоимость '))
    if price == 0:
        print('оплатите')
