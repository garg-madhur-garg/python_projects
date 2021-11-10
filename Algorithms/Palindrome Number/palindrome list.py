lstoriginal = []
for i in range(1, 5):
    inp = int(input(f"Enter number {i}\n"))
    lstoriginal.append(inp)
lstreverse = []
for originalj in lstoriginal:
    ori = originalj
    k = True
    while k:
        j = ori
        if j <= 10:
            lstreverse.append(j)
            k = False
        elif j > 10:
            # k = True
            reverse = 0
            while j != 0:
                remainder = j % 10
                reverse = reverse*10 + remainder
                j //= 10
            if reverse == originalj:
                lstreverse.append(reverse)
                k = False
            else:
                ori += 1

print(lstreverse)

# print(lstreverse)
