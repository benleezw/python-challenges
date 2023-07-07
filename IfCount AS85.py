f = open("if.txt", "r")
male_count = 0
female_count = 0
for x in f:
    if "if" in x or "If" in x:
        male_count += 1
f.close()

f = open("mam.txt", "r")
for r in f:
    if "if" in x or "If" in x:
        female_count += 1

if male_count > female_count:
    print("There are more 'if's in if.txt than mam.txt")
else:
    print("There are more 'if's in mam.txt than if.txt")
