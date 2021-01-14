'''This is funny friendship calculator'''


score = 0
name = input("Enter your first name and give space and enter second name\n").lower()

for character in name:
    if character in 'friendsforever':
        score += 10
    elif character in 'bcypqdxz':
        score += 5
    else:
        score += 0

if score >= 60:
    print(f"Your friendship score is {score}")
    print("Congratulations! you both are best friends")
else:
    print(f"Your friendship score is {score}")
