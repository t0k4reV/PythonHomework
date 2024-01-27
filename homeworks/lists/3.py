marks = [int(a) for a in input().split()]
sumOfMarks = marks.count(5) + marks.count(4) + marks.count(3)
print((sumOfMarks/len(marks))*100)
