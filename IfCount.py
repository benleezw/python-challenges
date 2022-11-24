Fcount = 0
Mcount = 0
with open("rudyard.txt", "r") as whole_file:
    for line in whole_file:
        if "_if_" in line or "If" in line:
            Mcount = Mcount + 1
with open("mam.txt", "r") as whole_file:
    for line in whole_file:
        if "_if_" in line or "If" in line:
            Fcount = Fcount + 1
print("Fcount =", Fcount)
print("Mcount =", Mcount)
