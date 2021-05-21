def evaluate(s, knowledge):
    new_s = ''
    idx_list = []
    i = 0
    
    dct = {k: v for k, v in knowledge}
    
    while i < len(s):
        if s[i] == '(':
            start = i
            for j in range(i, len(s)):
                if s[j] == ')':
                    end = j
                    break
            key = s[i+1:j]
            if key in dct.keys():
                new_s += dct[key]
            else:
                new_s += '?'
                
            i = j + 1
        else:
            new_s += s[i]
            i += 1

    return new_s
    

s = "hi(name)"
knowledge = [["a","b"]]
print(evaluate(s, knowledge))
