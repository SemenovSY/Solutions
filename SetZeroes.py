def setZeroes(matrix):
    
    l_matrix = len(matrix)
    l_str = len(matrix[0])
    z_pos = []
    
    for i in range(l_matrix):
        for j in range(l_str):
            if matrix[i][j] == 0:
                z_pos.append([i,j])

    for i in range(len(z_pos)):
        matrix[z_pos[i][0]] = [0 for j in range(l_str)]
        for j in range(l_matrix):
            matrix[j][z_pos[i][1]] = 0

    print(matrix)
