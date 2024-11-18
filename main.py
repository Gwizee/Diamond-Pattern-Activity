row = int(input("Enter the no. of rows: "))

if row % 2 == 0:
    half = row // 2
else:
    half = (row // 2) + 1
space = half - 1
for i in range(1,half + 1):
    for j in range(1,space + 1):
        print(end=" ")
    space = space - 1
    number = 1
    for j in range(2 * i - 1):
        print(end=str(number))
        number=number + 1
    print()
space = 1
for i in range(1,half+1):
    for j in range(1,space+1):
        print(end=" ")
    space = space+1
    number=1
    for j in range(1,2*(half-i)):
        print(end=str(number))
        number = number + 1
    print()