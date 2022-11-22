from time import sleep
fm = input("do you want to read the female or male version of the poem (f/m): ")
if fm == 'm':
    fm = "rudyard.txt"
elif fm == 'f':
    fm = "mam.txt"
with open(fm,"r") as whole_file:
   for line in whole_file:
        print(line,end="")
        sleep(2)