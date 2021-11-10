print("Based on   1$ = 76.50 rupees")


def R2D(n):
    try:
        return f"{(1/76.50)*n} $"
    except:
        return "0$"


def D2R(n):
    try:
        return f"{n*76.50} rupee"
    except:
        return "something wrong"


if __name__ == '__main__':
    while 1:
        conv = input("\nFor Rupee to Doller conversion  Press R\nFor Doller to Rupee conversion Press D\nPress q for Exit\n").capitalize()

        if conv == "R":
            rup = float(input("Enter Amount in rupee\n"))
            print(R2D(rup))
        elif conv == "D":
            dol = float(input("Enter Amount in doller\n"))
            print(D2R(dol))
        elif conv == "Q":
            quit()
        else:
            print("wrong input. Please try again")

