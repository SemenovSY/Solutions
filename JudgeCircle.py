def jusgeCircle(moves):
    dct = {"U" : 0, "D" : 0, "L" : 0, "R" : 0}
    
    for elem in moves:
        dct[elem] += 1

    values = list(dct.values())

    if values[0] == values[1] and values[2] == values[3]:
        return True

    else:
        return False

moves = ""
print(jusgeCircle(moves))
