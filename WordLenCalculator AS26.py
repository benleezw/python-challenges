txt = input("input text file for read: ")
wordcount = []
lettercount = 0
totalcount = 0
total = 0
avg = 0
space = " "
for i in range(0, len(txt)):
    if txt[i] != space:
        lettercount = lettercount + 1
        totalcount = totalcount + 1
    else:
        wordcount.append(lettercount)
        lettercount = 0
for r in range(0, len(wordcount)):
    total = total + wordcount[r]
avg = total/len(wordcount)
print("Average word count is"+space+str(int(avg)))

