line = list(input())
t = 0
for i in line:
    if line[t] == '-' and line[t+1] == '-':
        line[t], line[t+1] = '', '—'
    t += 1
print(''.join(line))