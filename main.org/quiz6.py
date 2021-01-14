num1 = int(input("enter which term you want to print\n"))


def fibonacii(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacii(n-1) + fibonacii(n-2)


print(fibonacii(num1))

