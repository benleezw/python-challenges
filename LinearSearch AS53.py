array = ["P", "y", "t", "h", "o", "n"]
item = input("item: ")
Found = False
arraypos = 0
print()
while arraypos != len(array) and Found == False:
    if array[arraypos] == item:
        print("Item is found at position "+str(arraypos)+" of array")
        Found = True
    else:
        arraypos = arraypos + 1
    if arraypos == len(array) and Found == False:
        print("Item is not in array")
