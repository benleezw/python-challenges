from random import randint
from time import sleep
from copy import copy

theArray = []

def generate_array(theArray, difficulty):
    difficulty = int(difficulty)
    if difficulty == 1:
        itemcount = 10
    if difficulty == 2:
        itemcount = 15
    if difficulty == 3:
        itemcount = 20
    if difficulty == 4:
        itemcount = 40
    for x in range (0, itemcount):
        item_to_add = randint(1,itemcount)
        while item_to_add in theArray:
            item_to_add = randint(1,itemcount + 10)
        theArray.append(item_to_add)
    print(theArray)
    return theArray

def bubblesort_dsc(theArray):
    # print("dsc")
    for r in range (0, len(theArray)):
        for i in range (0, len(theArray) - 1):
            if theArray[i] < theArray[i + 1]:
                temp = theArray[i]
                theArray[i] = theArray[i + 1]
                theArray[i + 1] = temp
    return theArray

def bubblesort_asc(theArray):
    # print("asc")
    for r in range (0, len(theArray)):
        for i in range (0, len(theArray) - 1):
            if theArray[i] > theArray[i + 1]:
                temp = theArray[i]
                theArray[i] = theArray[i + 1]
                theArray[i + 1] = temp
    return theArray

def question_generator(theArray):
    questions_answered = {}
    choice = int(input("Select Options \n1. Generate Question\n2. Leave \n"))
    if choice == 2:
        print("\n GoodBye...")
    else:
        while choice != 2:
            difficulty = input("\nDifficulty Selection \n1. Easy - 10 items \n2. Moderate - 15 items \n3. Annoying - 20 items \n4. Don't Select This\n")
            asc_dsc = int(input("\n1. Ascending \n2. Descending\n"))
            # print(difficulty)
            question = generate_array(theArray, difficulty)
            unsorted = copy(question)
            if asc_dsc == 1:
                solution = bubblesort_asc(question)
            if asc_dsc == 2:
                solution = bubblesort_dsc(question)
            questions_answered[str(unsorted)] = solution
            # print(question)
            sleep(5)
            show_solution = input("\nReveal Solution (Y/N)\n")
            if show_solution == "Y":
                print(solution)
                print()
                theArray = []
                choice = int(input("Select Options \n1. Continue\n2. Leave\n"))
            else:
                theArray = []
                choice = int(input("Select Options \n1. Continue\n2. Leave\n"))
        print("\n GoodBye...")
        print("\n Questions Answered:\n")
        index = 1
        for i in questions_answered:
            print("Question",str(index)+":", i, "Answer:",questions_answered[i],"\n")
            index += 1
question_generator(theArray)