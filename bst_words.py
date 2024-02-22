wordArr = ["grom", "crudge", "flim", "dromerd", "borumned", "carged", "loop", "zibrava", "ygdrasil"]


class Node:
    def __init__(self, data):
        self.__data = data
        self.__leftchild = None
        self.__rightchild = None

    def insert(self, data):
        if data < self.__data:
            if self.__leftchild:
                self.__leftchild.insert(data)
            else:
                self.__leftchild = Node(data)
        else:
            if self.__rightchild:
                self.__rightchild.insert(data)
            else:
                self.__rightchild = Node(data)

    def search(self, val):
        if val == self.__data:
            return str(val)+" in BST"
        elif val < self.__data:
            if self.__leftchild:
                return self.__leftchild.search(val)
            else:
                return str(val)+" not in BST"
        else:
            if self.__rightchild:
                return self.__rightchild.search(val)
            else:
                return str(val)+" not in BST"
    
    def printtree(self):
        if self.__leftchild:
            self.__leftchild.printtree()
        print(self.__data)
        if self.__rightchild:
            self.__rightchild.printtree()

root = Node("jubulon")
for i in wordArr:
    root.insert(i)

root.printtree()
print(root.search("borumned"))
print(root.search("sudie"))
