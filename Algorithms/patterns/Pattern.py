num1 = int(input("enter number of rows you want to print\n"))
num2 = bool(int(input("enter 0 or 1\n")))
if num2:
    i = 1
    while i <= num1:
        print(i*"*")
        i += 1
else:
    i = 4
    while i >= 1:
        print(i*"*")
        i -= 1




