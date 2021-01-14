import time

no_of_app = int(input("Enter number of apples harry have\n"))
mini = int(input("Enter minimum apples you want to check\n"))
maxi = int(input("Enter maximum apples you want to check\n"))
for i in range(mini, maxi+1):
    if no_of_app%i == 0:
        print("calculating...")
        time.sleep(1)
        print(f"{i} is a divisor of {no_of_app}")
    else:
        print("calculating...")
        time.sleep(1)
        print(f"{i} is not a divisor of {no_of_app}")
