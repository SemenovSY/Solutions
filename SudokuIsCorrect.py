def sudokuIsCorrect(sudoku):

    mt = []
    
    def check(sudoku):
        mt = []
        for arr in sudoku:
            for elem in arr:
                if elem != '.':
                    if elem in mt:
                        return False
                    else:
                        mt.append(elem)
            mt = []
        return True

    for i in range(len(sudoku[0])):
        for j in range(len(sudoku)):
            if sudoku[j][i] != '.':
                if sudoku[j][i] in mt:
                    return False
                else:
                    mt.append(sudoku[j][i])
        mt = []
        boxes = []
        
    for i in range(3):
        for j in range(3):
            box = []
            for x in range(3):
                for y in range(3):
                    box.append(sudoku[x+i*3][y+j*3])
            boxes.append(box)
    
    if check(sudoku) and check(boxes):
        return True
    else:
        return False

