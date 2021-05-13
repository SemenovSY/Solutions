def letterCombinations(digits):
    letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
               '8': 'tuv', '9': 'wxyz'}

    if digits:
        
        arr = ['']
        
        for digit in digits:
            string = []
            for val in arr:
                for alpha in letters[digit]:
                    string.append(val + alpha)

            arr = string
    else:
        arr = []

    return arr
