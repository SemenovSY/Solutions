def longestPalindrome(s):
    
    if len(s) == 1:
        return s
    
    else:
        substr = ''
        obr_substr = ''
        palin = ''
        l_palin = ''
        f_letter = ''
        for i in range(len(s)):
            f_letter = s[i]
            for j in range(1, len(s)):
                if s[i] == f_letter:
                    substr = s[i:j+1]
                    obr_substr = substr[::-1]
                    for k in range(len(substr)):
                        if substr[k] == obr_substr[k]:
                            next
                        else:
                            break
                    if k == len(substr) - 1:
                        palin = substr
                    if len(palin) > len(l_palin):
                        l_palin = palin
        return l_palin
