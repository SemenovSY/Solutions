def selectionSort(array):
    minElem = 0
    minIdx = 0
    length = len(array)
    for step in range(length):
        minElem = array[step]
        minIdx = step
        for i in range(step, length):
            if array[i] < minElem:
                minElem = array[i]
                minIdx = i
        array[minIdx] = array[step]
        array[step] = minElem

    return array


array = [1,2,5,2,8,3,5,9,3,1,7,0,3,2,27,9,4,2]
print(selectionSort(array))
