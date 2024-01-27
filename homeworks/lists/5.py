arr = [int(a) for a in input().split()]
s = False
for i in range(len(arr)-2):
    if arr[i+1]-arr[i] == arr[i+2]-arr[i+1]:
        s = True
    else:
        break
if s:
    print("Да")
else:
    print('Нет')
