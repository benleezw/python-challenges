from random import randint
from os import getcwd

class Employees:
    def __init__(self, FirstName, LastName, EmployeeID):
        self.__FirstName = FirstName # string
        self.__LastName = LastName # string
        self.__FullName = FirstName +" "+ LastName # string
        self.__Email = FirstName + LastName + "@gmail.com" # string
        self.__EmployeeID = EmployeeID # integer

    def getFirstName(self):
        return self.__FirstName
    def getLastName(self):
        return self.__LastName
    def getFullName(self):
        return self.__FullName
    def getEmail(self):
        return self.__Email
    def getID(self):
        return self.__EmployeeID
    
def readData():
    try:
        EmployeeArr = []
        linenum = 1
        EmployeeID = 0
        f = open("emailList.txt", "r")
        for line in f:
            if linenum == 1:
                FirstName = line.strip()
            if linenum == 2:
                LastName = line.strip()
                linenum = 0
                EmployeeArr.append(Employees(FirstName, LastName, EmployeeID))
                EmployeeID += 1
            linenum += 1
        f.close()
        return EmployeeArr
    except:
        print("File not in current dirrectory, "+getcwd())
    
EmployeeArr = readData()

def GetEmployeeEmail(EmployeeArr):
    SearchID = int(input("Enter ID to search for: "))
    for i in range (0, len(EmployeeArr) - 1):
        if EmployeeArr[i].getID() == SearchID:
            print(EmployeeArr[i].getID())
            print(EmployeeArr[i].getFullName())
            print(EmployeeArr[i].getEmail())

GetEmployeeEmail(EmployeeArr)
            