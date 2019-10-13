import quickSort

array1 = [4, 5, 3, 2, 0, 1, 18, 17, 100]
array2 = [9, 5, 7, 8, 6, 4, 100, 19, 18]
intersection = []

array1 = quickSort.quickSort(array1, 0, len(array1) -1)
array2 = quickSort.quickSort(array2, 0, len(array2) -1)

for i in range(0, len(array1)):
    for j in range(0, len(array2)):
        if(array1[i] == array2[j]):
            intersection.append(array1[i])
        elif(array2[j] > array1[i]):
            break

print(intersection)