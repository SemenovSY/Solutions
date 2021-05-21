def checkRepeats(arr):
    ans = []
    dct = {}
    
    for elem in arr:
        if elem not in dct.keys():
            dct[elem] = 0
        dct[elem] += 1
        
    for elem in dct.keys():
        if dct[elem] == 1:
            ans.append(elem)

    return ans

arr = [1,1,1,1,4,2,3,6,6,2,8,7,2,2,4,8,11,34]
print(checkRepeats(arr))
