marks = []
a = int(input())
while a != 0:
      marks.append(a)
      a = int(input())
print(100*(marks.count(3)+marks.count(4)+marks.count(5))/len(marks))

