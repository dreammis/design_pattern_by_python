def searchtt(alist, item):
    """

    """
    found = False
    index = 0

    while index < len(alist) and not found:
        if alist[index] == item:
            found = True
        else:
            index += 1
    return index


alist = [1, 23, 4, 45, 5, 6, 6, 7, 7, 88, 8, 6, 5, 4, 3, 3, 23, 2, 2, 22, 2, 2, 2]
print(searchtt(alist, 88))


def insertionSort(alist):
   for index in (1, len(alist)):
       value = alist[index]
       position = index
       while position >0 and alist[position-1] >value:
           alist[position] = alist[position -1]
           position -= 1
       alist[position] = value

alist = [54,26,93,17,77,31,44,55,20]

[17, 26, 54, 93]
insertionSort(alist)
print(alist)




class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())



