def bubbleSort(array):
    n = len(array)
    max_elem = 0
    max_idx = 0
    for step in range(n):
        max_elem = 0
        max_idx = 0
        for i in range(n - step - 1):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
    return array

array = [195, 48, 323, 217, 97, 36, 107, 423, 174, 393, 218, 268, 471, 421, 198, 477, 432, 452, 394, 8, 237, 227, 23, 184, 305, 304, 490, 41, 397, 106, 46, 343, 53, 197, 92, 209, 377, 115, 453, 245, 281, 356, 363, 85, 479, 84, 50, 477, 455, 98]
print(bubbleSort(array))
