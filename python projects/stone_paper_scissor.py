import random
import time

# Introduction
print("This is rock, paper and scissor game")
print("Rules of this game are: ")
print("Between rock and paper:  paper wins!\nBetween rock and scissor:  rock wins!\nBetween paper and scissor:  scissor wins!\n")
print("Game completed in 10 rounds\nLets begin!!\n")

# Computer's Input
lst = ["rock", "paper", "scissor"]
comp_choice = random.choice(lst)

pscore = 0
cscore = 0

# Game loop
for i in range(1, 11):
    print(f"\nRound no. {i}")
    play_choice = input("Enter your choice\n")

    if (play_choice == "rock") and (comp_choice == "rock"):
        print("tie, you and computer choose same choice {rock}")

    elif (play_choice == "rock") and (comp_choice == "paper"):
        print("Computer wins!!!")
        print(f"computer's choice was {comp_choice}")
        cscore += 5

    elif (play_choice == "rock") and (comp_choice == "scissor"):
        print("You wins!!!")
        print(f"Your choice was {play_choice}")
        pscore += 5

    elif (play_choice == "paper") and (comp_choice == "rock"):
        print("You wins!!!")
        print(f"Your choice was {play_choice}")
        pscore += 5

    elif (play_choice == "paper") and (comp_choice == "paper"):
        print("tie, you and computer choose same choice {paper}")

    elif (play_choice == "paper") and (comp_choice == "scissor"):
        print("Computer wins!!!")
        print(f"computer's choice was {comp_choice}")
        cscore += 5

    elif (play_choice == "scissor") and (comp_choice == "rock"):
        print("Computer wins!!!")
        print(f"computer's choice was {comp_choice}")
        cscore += 5

    elif (play_choice == "scissor") and (comp_choice == "paper"):
        print("You wins!!!")
        print(f"Your choice was {play_choice}")
        pscore += 5

    elif (play_choice == "scissor") and (comp_choice == "scissor"):
        print("tie, you and computer choose same choice {paper}")

    else:
        print("wrong input, Try again")

print("\nResult time. Please wait...")
time.sleep(4)

print(f"computer score is {cscore}\nyour score is {pscore}\n")

if pscore > cscore:
    print(f"Congratulations!!\nYou wins the game with score {pscore - cscore}")

elif pscore < cscore:
    print(f"Computer wins the game with score {cscore - pscore}")

else:
    print("Your and Computer scores are same.\nNobody wins")
