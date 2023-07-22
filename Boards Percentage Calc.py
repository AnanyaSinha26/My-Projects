from tabulate import tabulate

maths = float(input("Enter the marks of Maths out of hundred(in decimal): "))
eng = float(input("Enter the marks of English out of hundred(in decimal): "))
sst = float(input("Enter the marks of SST out of hundred(in decimal): "))
sci = float(input("Enter the marks of Science out of hundred(in decimal): "))
f = float(input("Enter the marks of French out of hundred(in decimal): "))
cs = float(input("Enter the marks of CS out of hundred(in decimal): "))

# total_marks = x

numbers = [maths,eng,sst,sci,f,cs]
numbers.sort(reverse=True)
numbers.pop()

# print(numbers)

x = sum(numbers)

print("Your total marks out of 500 is", x, ".")

y = x/5

print("Your overall percentage is", y)

Subjects = ["Maths", "English", "SST", "Science", "French", "CS","Total Marks", "Overall Percentage"]
Marks = [maths, eng, sst, sci, f, cs, x, y]

table = [[Subjects[i], Marks[i]] for i in range(len(Subjects))]

print(tabulate(table, headers=['Subjects', 'Marks'], tablefmt='orgtbl'))
