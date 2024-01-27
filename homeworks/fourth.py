line = list(input())
t = 0

for i in line:
    if i == "(" or i == ")" or i == " ":
        line[t] = ""
    t += 1
print(''.join((line)))


