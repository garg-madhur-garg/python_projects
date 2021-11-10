print("This program will give you the next palindrome of a number.")
userwants = int(input("How many number you want to test\n"))

for i in range(1, userwants + 1):
    number1 = int(input(f"Enter a number{i}\n"))
    num1 = number1
    while 1:
        a = num1 + 1
        original = a
        reverse = 0
        while a != 0:
            remainder = a % 10
            reverse = reverse*10 + remainder
            a = a // 10
        if original == reverse:
            print(f"Next palindrome of {number1} is {original}\n")
            break
        else:
            num1 += 1


