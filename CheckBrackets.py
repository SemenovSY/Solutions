def checkBrackets(string):
    brackets = {'(' : 0, ')' : 0}
    for elem in string:
        if elem in brackets.keys():
            brackets[elem] += 1

    return len(set(brackets.values())) == 1



string = '())))'
print(checkBrackets(string))
