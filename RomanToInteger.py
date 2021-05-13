def romanToInt(s):
    dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(s) < 2:
        return dct[s]
    
    integ = 0
    i = 0

    while i < len(s):
        if i != len(s)-1:
            if dct[s[i]] < dct[s[i+1]]:
                integ -= dct[s[i]]
            else:
                integ += dct[s[i]]
        else:
            integ += dct[s[i]]            
        i += 1        
    return integ

def integerToRom(num):
    dct = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

    x = num
    ans = ''
    i = 0
    lst_of_keys = list(dct.keys())[::-1]
    
    while num:
        if lst_of_keys[i] <= num:
            ans += dct[lst_of_keys[i]]
            num -= lst_of_keys[i]
                    
        else:
            i += 1

    return ans
