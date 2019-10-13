stringToCheck = '001000100000'

def countLongestZeros(stringToCheck):
    longestCount = 0
    currentCount = 0
    for char in stringToCheck:
        if(char == '0'):
            currentCount = currentCount + 1
            if(currentCount > longestCount):
                longestCount = currentCount
        else:
            currentCount = 0
    return longestCount

print(countLongestZeros(stringToCheck))

# line1 = '01110'
# line2 = '01110'
# line3 = '00000'
concatenatedLine = '011100111000000'
grid = [[None for i in range(5)] for j in range(3)]
for iterator in range(len(concatenatedLine)):
    print(concatenatedLine[iterator], end='')
    if(iterator % 5 == 4):
        print()
    grid[iterator//5][iterator%5] = concatenatedLine[iterator]

def findLongestZeroStringInGrid(listToSearch):
    longestCount = 0
    currentCount = 0
    ## keep track of visited spaces
    exploredGrid = [[False for i in range(len(listToSearch[0]))] for j in range(len(listToSearch))]
    xMax = len(listToSearch[0])
    yMax = len(listToSearch)
    for yPos in range(yMax):
        for xPos in range(xMax):
            if(not exploredGrid[yPos][xPos]):
                currentCount = currentCount + explore(listToSearch, exploredGrid, xPos, yPos, xMax -1, yMax -1)
                if(currentCount > longestCount):
                    longestCount = currentCount
    return longestCount
    
def explore(listToSearch, exploredGrid, xPos, yPos, xMax, yMax):
    if(not isOutOfBounds(xMax, yMax, xPos, yPos) and not exploredGrid[yPos][xPos]):
        exploredGrid[yPos][xPos] = True
        if(listToSearch[yPos][xPos] == '0'):
            return 1 + explore(listToSearch, exploredGrid, xPos -1, yPos, xMax, yMax) + \
            explore(listToSearch, exploredGrid, xPos +1, yPos, xMax, yMax) + \
            explore(listToSearch, exploredGrid, xPos, yPos -1, xMax, yMax) + \
            explore(listToSearch, exploredGrid, xPos, yPos + 1, xMax, yMax)
    return 0

## Assume 0 is minimum
def isOutOfBounds(xMax, yMax, x, y):
    if(x < 0 or y < 0 or x > xMax or y > yMax):
        return True
    return False

print(findLongestZeroStringInGrid(grid))
    