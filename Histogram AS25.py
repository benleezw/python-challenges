histolist = []
decision = input("would you like to add values to the histogram: ")
while decision != "n":
    addvalue = input("add a value to the histogram: ")
    histolist.append(addvalue)
    print()
    decision = input("add another value to the histogram: ")
print()

for i in range (0,len(histolist)):
    print("*" * int(histolist[i]))
    
