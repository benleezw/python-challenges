word_list = [] # words to sort
sorted_list = sorted(word_list)

f = open("Sorted List.txt", "x")
f.close()

f = open("Sorted List.txt", "w")
for word in sorted_list:
    f.write(word+"\n")
f.close()

