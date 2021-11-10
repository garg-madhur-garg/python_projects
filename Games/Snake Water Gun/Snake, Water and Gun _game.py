import random

print("This is snake, water and Gun game")
print("this game will played 10 times. At the end of the game more points will decide the winner.\n")
print("RULES are:\nBetween Snake and Water___Snakes win\nBetween Snake and Gun___Gun wins\nBetween Water and"
      " Gun___Water wins\nPlease write full name of choice in lowercase")

cscore = 0
pscore = 0
i = 1

while i <= 10:
    lst = ["snake", "gun", "water"]
    com = random.choice(lst)
    plr = input("\nwrite your choice\n")
    if(com == "snake" and plr == "gun") or (com == "water" and plr == "snake") or (com =="gun" and plr == "water"):
        print("you won")
        pscore += 10
        print(f"your score is {pscore}")
    elif(com == "snake" and plr == "snake") or (com == "water" and plr == "water") or (com =="gun" and plr == "gun"):
        print("you and computer choose same choice, So nobody gain points")
    else:
        print("computer won")
        cscore += 10
        print(f"computer score is {cscore}")
    i += 1

print("\n\n\n")
print(f"your score is {pscore}")
print(f"computer score is {cscore}")

if pscore > cscore:
    print("you win the game")
else:
    print("computer won the game")
