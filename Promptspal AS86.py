from random import randint

f = open("promptspal.txt", "r")
prompts = []
for x in f:
    prompts.append(x)

print(prompts[randint(1,len(prompts))])

f.close()
