def addBinary(a, b):
    
    c = ''
    st = '0'

    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    else:
        a = '0' * (len(b) - len(a)) + a
        

    for i in range(1, len(a)+1):
        if a[-i] == '1':
            if b[-i] == '1':
                if st == '1':
                    c += '1'
                else:
                    c += '0'
                    st = '1'
            else:
                if st == '1':
                    c += '0'
                else:
                    c += '1'
        else:
            if b[-i] == '1':
                if st == '1':
                    c += '0'
                else:
                    c += '1'
            else:
                if st == '1':
                    c += '1'
                    st = '0'
                else:
                    c += '0'
        
    if st == '1':
            c += '1'

    return c[::-1]  
