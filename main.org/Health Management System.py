num1 = int(input("enter 1 for Rishab\nenter 2 for Rohan\nenter 3 for Tushar\n"))
if num1 == 1:
    num2 = int(input("enter 1 for Add\nenter 2 for Retrieve\n"))
    if num2 == 1:
        num3 = int(input("enter 1 for Dish\nenter 2 for Exercise\n"))
        if num3 == 1:
            with open("Rishab_diet.txt", "a") as f:
                diet = input("enter your dish name\n")
                f.write(diet + "\n")
        else:
            with open("Rishab_exercise.txt", "a") as f:
                exer = input("enter your exercise name\n")
                f.write(exer + "\n")
    if num2 == 2:
        num4 = int(input("enter 1 for Dish\nenter 2 for Exercise\n"))
        if num4 == 1:
            with open("Rishab_diet.txt") as f:
                print(f.read())
        else:
            with open("Rishab_exercise.txt") as f:
                print(f.read())
if num1 == 2:
    num2 = int(input("enter 1 for Add\nenter 2 for Retrieve\n"))
    if num2 == 1:
        num3 = int(input("enter 1 for Dish\nenter 2 for Exercise\n"))
        if num3 == 1:
            with open("Rohan_diet.txt", "a") as f:
                diet = input("enter your dish name\n")
                f.write(diet + "\n")
        else:
            with open("Rohan_exercise.txt", "a") as f:
                exer = input("enter your exercise name\n")
                f.write(exer + "\n")
    if num2 == 2:
        num4 = int(input("enter 1 for Dish\nenter 2 for Exercise\n"))
        if num4 == 1:
            with open("Rohan_diet.txt") as f:
                print(f.read())
        else:
            with open("Rohan_exercise.txt") as f:
                print(f.read())
if num1 == 3:
    num2 = int(input("enter 1 for Add\nenter 2 for Retrieve\n"))
    if num2 == 1:
        num3 = int(input("enter 1 for Dish\nenter 2 for Exercise\n"))
        if num3 == 1:
            with open("Tushar_diet.txt", "a") as f:
                diet = input("enter your dish name\n")
                f.write(diet + "\n")
        else:
            with open("Tushar_exercise.txt", "a") as f:
                exer = input("enter your exercise name\n")
                f.write(exer + "\n")
    if num2 == 2:
        num4 = int(input("enter 1 for Dish\nenter 2 for Exercise\n"))
        if num4 == 1:
            with open("Tushar_diet.txt") as f:
                print(f.read())
        else:
            with open("Tushar_exercise.txt") as f:
                print(f.read())