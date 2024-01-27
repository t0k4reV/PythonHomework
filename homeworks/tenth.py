line = '123 456'
lst = list(line.split(' '))
lst[0], lst[1] = lst[1], lst[0]
print(lst[0], lst[1])
