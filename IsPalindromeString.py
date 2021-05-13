def isPalindrome(s):
    if len(s) == 1:
        return True
    
    new_s = ''
    
    for elem in s:
        if elem.isalpha() or elem.isdigit():
            new_s += elem

    new_s = new_s.lower()

    return new_s = new_s[::-1]

print(isPalindrome('A man, a plan, a canal: Panama'))

    
            
