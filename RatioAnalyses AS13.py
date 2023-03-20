choice = input("GPM or NPM?: ")
choice.lower
if choice == "gpm":
    grossprofit = int(input("input gross profit: "))
    sales = int(input("input sales: "))
    GPM = (grossprofit/sales) * 100
    print("Gross profit is"+" "+str(GPM)+"%")
elif choice == "npm":
    netprofit = int(input("input net profit: "))
    sales = int(input("input sales: "))
    NPM = (netprofit/sales) * 100
    print("Net profit is"+" "+str(NPM)+"%")
