word = input("input word: ")
vowels = ['a','e','i','o','u']
vowelcount = 0

for i in range(0, len(word)):
    if word[i] in vowels:
        vowelcount = vowelcount + 1
if vowelcount > 1:
    print("The word " + word + " has " + str(vowelcount) + " vowels")
else:
    print("The word " + word + " has a vowel")
