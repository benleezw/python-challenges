from random import choice
wordbank = ["econs", "good", "bad", "he", "she", "work", "well", "doesn't", "hope", "I", "will", "continue", "poorly", "does", "with", "others", "economics"]
student_count = int(input("Enter number of students in the class: "))
print()
comment = ""
for i in range (0, student_count):
    for r in range (0, 12):
        comment += choice(wordbank)+" "
    print(comment)
    print()
    comment = ""
