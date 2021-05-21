def mergeSort(array):
    array = list(array)
    if len(array) == 1:
        yield array
    middle = len(array) // 2
    firstHalf = mergeSort(array[0: middle])
    secondHalf = mergeSort(array[middle:])
    sortedArray = []
    i = 0
    j = 0
    while i < len(firstHalf) and j < len(secondHalf):
        if firstHalf[i] < secondHalf[j]:
            sortedArray.append(firstHalf[i])
            i += 1
        else:
            sortedArray.append(secondHalf[j])
            j += 1

    while i < len(firstHalf):
        sortedArray.append(firstHalf[i])
        i += 1

    while j < len(secondHalf):
        sortedArray.append(secondHalf[j])
        j += 1
        
    yield from gen(sortedArray)

array = [1,6,3,2,7,83,4,7]
array = list(array)
for item in mergeSort(array):
    print(item)
