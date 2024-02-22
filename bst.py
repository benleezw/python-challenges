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

root = Node(56)
root.insert(23)
root.insert(92)
root.insert(74)
root.insert(43)
root.insert(12)
root.insert(34)
root.insert(6)
root.insert(89)
root.printtree()
print(root.search(2))
print(root.search(56))
