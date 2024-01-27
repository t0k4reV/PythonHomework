a = input().split()
tmp = [item for item in a if item.find('@') != -1]
print(tmp[0])
