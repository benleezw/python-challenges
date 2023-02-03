from random import randint
special = "!@#$%^&*()_+-=<>?/.,;:'\"|[]{}~`"
colour = input("Input a favourite colour: ")
place = input("Input a favourite place: ")
animal = input("Input a favourite animal: ")
pass1 = colour + place + animal
pass2 = ""
length = len(pass1)
for i in range(0, length):
    randpos = randint(0, len(pass1)-1)
    pass2 = pass2 + pass1[randpos]
    pass1 = pass1.replace(pass1[randpos], "", 1)
pass2 = pass2 + special[randint(0, len(special))]
print(pass2)
