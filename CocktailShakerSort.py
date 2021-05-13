def cocktailShakerSort(array):
    for step in range(len(array)//2):
        for i in range(step, len(array)-step-1):
            if array[i] > array[i+1]:
                array[i+1], array[i] = array[i], array[i+1]
        for i in range(len(array)-step-1, step+1, -1):
            if array[i] < array[i-1]:
                array[i-1], array[i] = array[i], array[i-1]
    return array

print(cocktailShakerSort(array))
