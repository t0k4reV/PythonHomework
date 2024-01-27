line = 'Экономический рост связан с магическая силой президента армении'
x = line.find('ический')
a = list(line)
a[x: x+7] = '.'
line = ''.join(a)
y = line.find('ическая')
a = list(line)
a[y: y+7] = '.'
line = ''.join(a)
print(line)


