import re

mystr = "913681804461, 918807391277, 915310738988, 919937447529, 911931184509, 918661044426, 916476433605," \
        " 919206046303, 919689093020"

patt = re.compile(r"\b91")
match = patt.finditer(mystr)
for matches in match:
    print(matches)

