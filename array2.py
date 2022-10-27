checker = []
row = []
newrow = []
cross = False

n = int(input("input length: "))
m = int(input("input width: "))
for i in range(0, n):
    if cross == False:
        row.append(".")
        newrow.append("*")
        cross = True
    elif cross == True:
        row.append("*")
        newrow.append(".")
        cross = False

for x in range(0, m):
    checker.insert(x, row)
for c in range(0,m):
    checker.insert(c*2, newrow)
for r in range(0, m):
    print(*checker[r])