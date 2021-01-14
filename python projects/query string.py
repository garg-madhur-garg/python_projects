import re

sentences = ["this is good", "python is good", "python is not python snake"]
query = input("Enter query string\n")

# patt = re.compile(query)
# matches = patt.finditer(str(sentences))
matches = re.search(query, str(sentences))

# for match in matches:
i = 1
while i:
    print(matches.string[i])
    i += 1
    if i == 4:
        quit()
