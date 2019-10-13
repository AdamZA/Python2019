listToFilter = [1,2,3,4,5,6,7,8,9,10]

def checkEvenNumbers(numberToCheck):
    if(numberToCheck % 2 == 0):
        return True
    return False

## Convert an Iterator to a List + Use Filter method on list
result = list(filter(checkEvenNumbers, listToFilter))
print(result)

## Construct a Dictionary
dictionary = {
'Jan' : 1,
'Feb' : 2
}

print(dictionary['Jan'])

## Print out a dictionary
for x, y in dictionary.items():
    print (x, y)

## Check if value in dictionary
print ('Jan' in dictionary)

## Variations on find intersection:
array1 = [4, 5, 3, 2, 0, 1, 18, 17, 100]
array2 = [9, 5, 7, 8, 6, 4, 100, 19, 18]
intersection = []

for x in array2:
    if(x in array1):
        intersection.append(x)

print(intersection)

## 2D array

x,y = 10, 10
board = [[False for i in range(x)] for j in range(y)]
print(board[0][0])