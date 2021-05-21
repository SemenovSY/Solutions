def evaluate(s, knowledge):
    new_s = ''
    idx_list = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            start = i
            for j in range(i, len(s)):
                if s[j] == ')':
                    end = j
                    break
            key = s[i+1:j]
            fl = 0
            for k in range(len(knowledge)):
                if knowledge[k][0] == key:
                    fl = 1
                    new_s += knowledge[k][1]
                    break
            if fl != 1:
                new_s += '?'
            i = j + 1
        else:
            new_s += s[i]
            i += 1

    return new_s
    

s = "hi(name)"
knowledge = [["a","b"]]
print(evaluate(s, knowledge))
