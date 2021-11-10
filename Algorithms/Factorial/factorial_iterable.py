num1 = int(input("Enter an integer which you want to calculate factorial\n"))


def factorial_iterable(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


def trailling_zero(n):
    count = 0
    i = 5
    while n/i >= 1:
        count += int(n/i)
        i *= 5
    return count


if __name__ == '__main__':
    # # print(trailling_zero(num1))
    # print(factorial_iterable(num1))
    print(f"factorial of {num1} is = {factorial_iterable(num1)}\nand no. of trailing zeros are {trailling_zero(num1)}")