def removeDuplicates(arr):
    i = 0
    while i < len(arr):
        if len(arr) == 1:
            return print(f'{len(arr)}, nums = {arr}')
        elif arr[i] == arr[i-1]:
            arr.pop(i)
        else:
            i += 1

    return print(f'{len(arr)}, nums = {arr}')
