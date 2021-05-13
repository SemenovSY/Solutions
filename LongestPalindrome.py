def longestPalindrome(s):
    
    l_pal = ''
    l_pal_len = 0

    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > l_pal_len:
                l_pal = s[left:right+1]
                l_pal_len = right - left + 1

            left -= 1
            right += 1

    for i in range(len(s)):
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > l_pal_len:
                l_pal = s[left:right+1]
                l_pal_len = right - left + 1

            left -= 1
            right += 1
    return l_pal
