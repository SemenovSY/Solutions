def groupAnagrams(strs):
    tmp = strs.copy()
    dct = {}
    for i in range(len(tmp)):
        tmp[i] = ''.join(sorted(tmp[i]))
        if tmp[i] not in dct:
            dct[tmp[i]] = [strs[i]]
        else:
            dct[tmp[i]].append(strs[i])

    return list(dct.values())
    
strs = []
print(groupAnagrams(strs))
