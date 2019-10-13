import queue

## Take in a list, and a search term
array1 = [4, 5, 3, 2, 0, 1, 18, 17, 100]
array2 = [5, 3, 7, 2, 4, 6, 8, 1, 9]

## Construct a tree of nodes. Each node will have 0-2 children.
class Node:
    def __init__(self, nodeValue):
        self.nodeValue = nodeValue
        self.leftChild = None
        self.rightChild = None

## Insert method: Recursive call which travels the nodes until it reaches the bottom, then inserts
    def addChild(self, insertValue):
        if(insertValue > self.nodeValue):
            if(self.rightChild == None):
                self.rightChild = Node(insertValue)
            else:
                self.rightChild.addChild(insertValue)
        else:
            if(self.leftChild == None):
                self.leftChild = Node(insertValue)
            else:
                self.leftChild.addChild(insertValue)

## Search method: Recursive call to search the tree based on the search term
    def searchForValue(self, searchValue):
        if(self.nodeValue == searchValue):
            return True
        elif(searchValue > self.nodeValue):
            if(self.rightChild == None):
                return False
            else:
                return self.rightChild.searchForValue(searchValue)
        else:
            if(self.leftChild == None):
                return False
            else:
                return self.leftChild.searchForValue(searchValue)

    def printDepthFirst(self):
        print('PRINTING DEPTH FIRST')
        self.depthFirstRecursor()

    def depthFirstRecursor(self):
        print(self.nodeValue)
        if(self.leftChild != None):
            self.leftChild.depthFirstRecursor()
        if(self.rightChild != None):
            self.rightChild.depthFirstRecursor()
        

    ## Variants: Depth first vs Breadth first etc

    def printBreadthFirst(self, nodeQueue):
        print('PRINTING BREADTH FIRST')
        nodeQueue.put(self)
        while(nodeQueue.qsize() != 0):
            nextItem = nodeQueue.get()
            print(nextItem.nodeValue)
            if(nextItem.leftChild != None):
                nodeQueue.put(nextItem.leftChild)
            if(nextItem.rightChild != None):
                nodeQueue.put(nextItem.rightChild)

def searchWithBST(listToSearch, searchTerm):
    rootNode = Node(listToSearch[0])
    for iterator in range(1, len(listToSearch)):
        rootNode.addChild(listToSearch[iterator])

    rootNode.printBreadthFirst(queue.Queue())
    rootNode.printDepthFirst()
    return rootNode.searchForValue(searchTerm)

print(searchWithBST(array2, 10))