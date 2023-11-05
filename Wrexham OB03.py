from os import getcwd

class Wrexham:
    def __init__(self, playernum, playerforename, playersurname, position):
        self.__PlayerNumber = playernum #integer
        self.__Forename = playerforename #string
        self.__Surname = playersurname #string
        self.__Position = position #integer
        self.__CommunityInvolvement = 0
        self.__Injured = False

    def setCInvolvement(self, change):
        self.__CommunityInvolvement += change

    def setInjured(self, PlayerNumPos):
        self.__Injured = not(wrexhamArr[PlayerNumPos].getInjured())

    def getPNum(self):
        return self.__PlayerNumber
    def getPFName(self):
        return self.__Forename
    def getPSName(self):
        return self.__Surname
    def getPos(self):
        return self.__Position
    def getCInvolvement(self):
        return self.__CommunityInvolvement
    def getInjured(self):
        return self.__Injured

def readData():
    try:
        f = open("wrexham.txt", "r")
        linenum = 1
        wrexhamArr = []
        for line in f:
            if linenum == 1:
                playernum = line
            if linenum == 2:
                playerforename = line
            if linenum == 3:
                playersurname = line
            if linenum == 4:
                position = line
                wrexhamArr.append(Wrexham(playernum, playerforename, playersurname, position))
                linenum = 0
            linenum += 1
        f.close()
        return wrexhamArr
    except:
        print("File not found, current directory is "+getcwd())

wrexhamArr = readData()
# print(wrexhamArr)

def changeCommInvolvement(wrexhamArr, PlayerNumPos, change):
    wrexhamArr[PlayerNumPos].setCInvolvement(change)

def ChangeInjured(wrexhamArr, PlayerNumPos):
    wrexhamArr[PlayerNumPos].setInjured(PlayerNumPos)

def getPlayerInfo(wrexhamArr):
    SelectPlayerNum = int(input("Enter Player Number: "))
    try:
        for i in range(0, len(wrexhamArr) - 1):
            # print(int((wrexhamArr[i].getPNum())))
            if SelectPlayerNum == int(wrexhamArr[i].getPNum()):
                PlayerNumPos = i
                # print(PlayerNumPos)
        print((str(wrexhamArr[PlayerNumPos].getPFName())).strip()+" "+str(wrexhamArr[PlayerNumPos].getPSName()))
        print(wrexhamArr[PlayerNumPos].getPos())
        print(wrexhamArr[PlayerNumPos].getCInvolvement())
        print(wrexhamArr[PlayerNumPos].getInjured())
        change = int(input("Enter change in community involvement: "))
        changeCommInvolvement(wrexhamArr, PlayerNumPos, change)
        change_injured = input("Change player's injured status?: ")
        if change_injured == "yes":
            ChangeInjured(wrexhamArr, PlayerNumPos)

        print((str(wrexhamArr[PlayerNumPos].getPFName())).strip()+" "+str(wrexhamArr[PlayerNumPos].getPSName()))
        print(wrexhamArr[PlayerNumPos].getPos())
        print(wrexhamArr[PlayerNumPos].getCInvolvement())
        print(wrexhamArr[PlayerNumPos].getInjured())

    except:
        print("Player number not in team")

getPlayerInfo(wrexhamArr)