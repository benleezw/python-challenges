monsterinfo = {}
f = open("monster info.txt", "r")
key = ""
value = ""
for line in f:
    comma = False
    for i in range (0, len(line) - 2):
        if comma == False:
            if line[i] == ',':
                comma = True
            else:
                key = key + line[i]
        else:
            value = value + line[i]
    monsterinfo[key] = value
    key = ""
    value = ""
f.close()

print(monsterinfo)