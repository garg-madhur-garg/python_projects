sum = 0
while True:

    userInput = input("Enter your amount or Press q for quit\n").capitalize()
    if userInput != "Q":
        sum = sum + int(userInput)
    else:
        print(f"Your total bill is {sum}")
        print("Thanks for shopping with us.")
        break
        