age = int(input("Enter your age\n"))


def when_100(n):
    rem = 100 - n
    return 2020 + rem - 1


if __name__ == '__main__':
    if age <=0:
        print("you are not yet born")
    elif 100 > age > 0:
        print("you will turn 100 year in ", when_100(age))
    elif age>=100:
        print("you seem to be the oldest person alive")
    else:
        print("shi input dal nhi to tujhe aaj hi 100 saal ka bna dunga")

    opt = input("If you want to know your age in any particular year then press y\nIf you want to quit then press any other key\n")
    if opt == "y":
        year = int(input("Enter the year"))
        print(year - 2020 + age)
    else:
        quit()