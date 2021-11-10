print("This is Indian Kirana Calculator")


def operation(n):
    if n == "A":
        return num1 + num2
    elif n == "S":
        return num1 - num2
    elif n == "M":
        return num1 * num2
    elif n == "D":
        return num1 / num2
    else:
        return "Wrong Input. Please try again"


if __name__ == '__main__':
    while 1:
        num1 = int(input("Enter first number\n"))
        num2 = int(input("Enter second number\n"))
        opt = input("\nPress A for ADD\nPress S for SUBTRACT\nPress M for MULTIPLY\nPress D for DIVIDE\n").capitalize()
        print(operation(opt))


