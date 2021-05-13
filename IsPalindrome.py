def isPalindrome(self, x: int) -> bool:
    xx = x
    if x < 0: 
        return False
    else: 
        y = 0
        while x >= 10:  
            y = y * 10 + x % 10
            x = x // 10
        y = y * 10 + x

        return xx == y
