import random
a = int(input("Enter the value of a\n"))
b = int(input("Enter the value of b\n"))

n = random.randint(a+1, b-1)


def game_loop():
    print("Player 1's turn:")
    i = 1
    global n
    while i:
        num = int(input(f"Please guess the number between {a} and {b}\n"))
        if num > n:
            print("Wrong guess, Enter a smaller number")
        elif num < n:
            print("Wrong guess, Enter a bigger number")
        else:
            print(f"Correct you took {i} trials to guess the number\n")
            print("Player 2's turn:")

            n = random.randint(a + 1, b - 1)       # Change the value of n for second player
            j = 1
            while j:
                num = int(input(f"Please guess the number between {a} and {b}\n"))
                if num > n:
                    print("Wrong guess, Enter a smaller number")
                elif num < n:
                    print("Wrong guess, Enter a smaller number")
                else:
                    print(f"Correct you took {j} trials to guess the number\n")
                    if i < j:
                        print("Player 1 wins!!")
                        quit()
                    elif i > j:
                        print("Player 2 wins!!")
                        quit()
                    else:
                        print("Game tie. Play again\n")
                        game_loop()
                j += 1
        i += 1


game_loop()
