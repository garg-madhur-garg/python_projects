
inp = int(input("Enter an integer\n"))
sum = 0
n = inp

while n > 0:
    sum = sum + (n % 10)*(n % 10)*(n % 10)
    n = int(n/10)

if sum == inp:
    print("Yes! it's armstrong number")
else:
    print("No! it's not armstrong number")
