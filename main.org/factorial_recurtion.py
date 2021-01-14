num1 = int(input("Enter an integer which you want to calculate factorial\n"))


def fact_recurtion(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact_recurtion(n-1)


if __name__ == '__main__':
    print(fact_recurtion(num1))
