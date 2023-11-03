import turtle
from os import getcwd


class pattern():
    def __init__(self, angle: int, times: int):
        self.__angle = angle # Integer
        self.__times = times # Integer

    def getAngle(self):
        return self.__angle
    
    def getTimes(self):
        return self.__times

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  # setting window dimensions
        turtle.bgcolor('black')
        for x in range(int(self.__times)):
            turtle.speed(500)
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(int(self.__angle))
        turtle.done()

def ReadFile():
    try:
        f = open("patterns.txt", "r")
        line_num = 1
        patternArr = []
        for line in f:
            if line_num == 1:
                angle = line
            if line_num == 2:
                times = line
                patternArr.append(pattern(angle, times))
                line_num = 0
            line_num += 1
        return patternArr
    except:
        print("File not found, current directory is "+getcwd())

patternArr = ReadFile()
pattern_choice = int(input("Enter pattern number: "))
pattern_choice -= 1
mypattern = pattern(patternArr[pattern_choice].getAngle(), patternArr[pattern_choice].getTimes())  # Demo pattern
mypattern.draw_pattern()