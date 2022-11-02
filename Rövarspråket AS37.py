from string import punctuation
string = input("input string: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
space = " "
num = []
for r in range(0, 10):
    num.append(str(r))

for i in range(0, len(string)):
    if string[i] not in vowels and string[i] != space and string[i] not in num and string[i] not in punctuation:
        newstring = string[i] + "o" + string[i]
    else:
        newstring = string[i]
    print(newstring, end="")

print()

