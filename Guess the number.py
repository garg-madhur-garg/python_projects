import random

n = random.randint(1, 99)
i = 0
print("number between 0 and 100")
print("This is game in which you will guess the number which i already choose. You have only 9 guesses")
while i <= 9:
    if i == 9:
        print("Game Over")
    else:
        g1 = int(input("guess the number\n"))
        if g1 == n:
            print("congratulation! you won the game")
            break
        elif g1 > n:
            print("sorry but actual number is lesser then", g1)
        else:
            print("sorry but actual number is greater then", g1)
        print("you have left", 8-i, "guesses")
    i += 1