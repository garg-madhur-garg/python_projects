print("Try to understand the topic comprehensions")
inp1 = int(input("Enter how many items you want to add\n"))
print("Enter name of items")
items = []
for i in range(inp1):
    inp2 = (input())
    items.append(inp2)
inp3 = int(input("Enter type of comprehension in which you want to display your items\n"
             "1. List Comprehension(press 1)\n2. Dictionary Comprehension(press 2)\n3. Set Comprehension(press 3)\n"))
if inp3 == 1:
    ls = [item for item in items]
    print(ls)
elif inp3 == 2:
    dic = {i: items[i] for i in range(inp1)}
    print(dic)
elif inp3 == 3:
    setc = {item for item in items}
    print(setc)
else:
    print("WRONG INPUT")


