def quickSort(arr, lo, hi):
    returnValue = arr
    if(hi > lo):
        partitionIndex = partition(returnValue, lo, hi)
        quickSort(returnValue, lo, partitionIndex-1)
        quickSort(returnValue, partitionIndex+1, hi)
    return returnValue

def partition(arr, lo, hi):
    index = lo - 1
    for iterator in range(lo, hi):
        if(arr[iterator] < arr[hi]):
            index = index + 1
            temp = arr[index]
            arr[index] = arr[iterator]
            arr[iterator] = temp
    
    temp = arr[index + 1]
    arr[index + 1] = arr[hi]
    arr[hi] = temp
    return index + 1