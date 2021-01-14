with open("currency")as f:
    lines = f.readlines()
currency_dic = {}
for line in lines:
    parsed = line.split("\t")
    currency_dic[parsed[0]] = parsed[1]
print(currency_dic)
amount = float(input("Enter amount"))
print("In which currency you want to convert. Available options are!!")
for nee in currency_dic.keys():
    print(nee)

curry = input("\nEnter one of these value\n")
print(f"the {amount} INR is equal to {amount*float(currency_dic[curry])} {curry}")

