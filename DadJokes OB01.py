from random import randint
from os import getcwd

class DadJokes:
    def __init__(self, prompt, answer):
        self.__prompt = prompt
        self.__answer = answer

    def getPrompt(self):
        return self.__prompt
    
    def getAnswer(self):
        return self.__answer
    
def readFile():
    try:
        f = open("DadJokes.txt", "r")
        DadJokesArr = []
        line_num = 1
        for line in f:
            # print(line)
            if line_num == 1:
                prompt = line
                # print(prompt)
            if line_num == 2:
                answer = line
                # print(answer)
                DadJokesArr.append(DadJokes(prompt, answer))
                line_num = 0
            line_num += 1
        return DadJokesArr
    except:
        print("File not Found, current directory is"+" "+getcwd())

def PrintRandomJoke(DadjokesArr):
    joke_choice = randint(0, len(DadjokesArr) - 1)
    joke_prompt = DadjokesArr[joke_choice].getPrompt()
    joke_answer = DadjokesArr[joke_choice].getAnswer()
    print(joke_prompt)
    input()
    print()
    print(joke_answer)

DadJokesArr = readFile()
PrintRandomJoke(DadJokesArr)