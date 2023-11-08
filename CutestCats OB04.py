class CutestCats:
    def __init__(self, name, description, weight, length, life, imageurl):
        self.__name = name
        self.__description = description
        self.__weight = weight
        self.__length = length
        self.__life = life
        self.__imageurl = imageurl

    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__description
    def getWeight(self):
        return self.__weight
    def getLength(self):
        return self.__length
    def getLife(self):
        return self.__life
    def getImageURL(self):
        return self.__imageurl
    
def GetCatDetails():
    CutestCatsArr = []
    f = open("CutestCats.txt", "r")
    for line in f:
        space_count = 0
        for r in range(0, len(line) - 1):
            if line[r] == " ":
                space_count += 1
        if space_count < 2 and len(line) > 1 and "https" not in line:
            name = line.strip()
            # print(name.strip())
        if ":" not in line and len(line) > 100:
            description = line.strip()
            # print(description.strip())
        if "WEIGHT" in line:
            weight = line[8:].strip()
            # print(weight.strip())
        if "LENGTH" in line:
            length = line[8:].strip()
            # print(length.strip())
        if "LIFE EXPECTANCY" in line:
            life = line[17:].strip()
            # print(life.strip())
        if "https://" in line:
            imageurl = line
            CutestCatsArr.append(CutestCats(name, description, weight, length, life, imageurl))
            space_count = 0
    f.close()
    return CutestCatsArr

CutestCatsArr = GetCatDetails()
# print(CutestCatsArr[2].getName())
# print(CutestCatsArr[2].getDescription())
# print(CutestCatsArr[2].getWeight())
# print(CutestCatsArr[2].getLength())
# print(CutestCatsArr[2].getLife())


def GetCatLife(CutestCatsArr):
    CatNameSearch = str(input("Enter Cat Name to search for: "))
    for i in range(0, len(CutestCatsArr) - 1):
        if CatNameSearch == (CutestCatsArr[i].getName()).strip():
            print("Name: "+CatNameSearch)
            print("Life Expectancy: "+str(CutestCatsArr[i].getLife()))


GetCatLife(CutestCatsArr)