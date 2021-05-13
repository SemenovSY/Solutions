def lols(s):
    
    sub_first = ''
    sub_second = ''
    i = 0
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    
    while i < len(s):
        if s[i] not in sub_first:
            sub_first += s[i]
            i += 1
        else:
            i = i - len(sub_first) + 1
            if len(sub_first) > len(sub_second):
                sub_second = sub_first
            sub_first = ''
            
    return max(len(sub_first), len(sub_second))
