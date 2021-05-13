def longestCommonPrefix(self, strs: List[str]) -> str:
        lg_prf = ''
        prf = ''
        kol = 0
        if len(strs) == 0:
            return ''

        if strs[0]:
            for i in range(len(strs[0])):
                kol = 0
                prf += strs[0][i]
                for string in strs:
                    if prf == string[:i+1]:
                        kol += 1
                if kol == len(strs):
                    lg_prf = prf

        return lg_prf
