def maxLength(arr):
    length = len(arr)
    if length == 1:
        return (len(arr[0]))

    maxLen = 0
    uniq = ['']

    for word in arr:
        for j in uniq:
            tmp = word + j
            if len(set(tmp)) == len(tmp):
                uniq.append(tmp)
                maxLen = max(maxLen, len(tmp))

    return maxLen
                
                
arr = ["ab","cd","cde","cdef","efg","fgh","abxyz"]
print(maxLength(arr))
