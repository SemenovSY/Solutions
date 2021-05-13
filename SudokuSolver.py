class SudokuSolver():
    def sudokuSolver(board):
        while True:
            minValCell = None
            for rowIndex in range(9):
                for columnIndex in range(9):
                    if board[rowIndex][columnIndex] == 0:
                        possibleValues = SudokuSolver.getPossibleValues(rowIndex, columnIndex, board)
                        possibleValuesCount = len(possibleValues)
                        if possibleValuesCount == 0:
                            return False
                        if possibleValuesCount == 1:
                            board[rowIndex][columnIndex] = possibleValues.pop()
                        if not minValCell or possibleValuesCount < len(minValCell[1]):
                            minValCell = ((rowIndex, columnIndex), possibleValues)

            if not minValCell:
                return True
            elif len(minValCell[1]) > 1:
                break

        i, j = minValCell[0]
        for elem in minValCell[1]:
            solution = board
            solution[i][j] = elem
            if SudokuSolver.sudokuSolver(solution):
                for k in range(9):
                    for l in range(9):
                        board[k][l] = solution[k][l]
                return True
        return False

    def getPossibleValues(rowIndex, columnIndex, board):
        possibleValues = {v for v in range(1,10)}
        possibleValues -= SudokuSolver.getRowValues(rowIndex, board)
        possibleValues -= SudokuSolver.getColumnValues(columnIndex, board)
        possibleValues -= SudokuSolver.getBoxValues(rowIndex, columnIndex, board)

        return possibleValues
        
        
    def getRowValues(rowIndex, board):
        return set(board[rowIndex][:])
        

    def getColumnValues(columnIndex, board):
        return {board[i][columnIndex] for i in range(9)}

    def getBoxValues(rowIndex, columnIndex, board):
        
        BoxRow = 3 * (rowIndex // 3)
        BoxColumn = 3 * (columnIndex // 3)

        return {board[BoxRow + r][BoxColumn + m] for r in range(3) for m in range(3)}

            
        
            
                
board = [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]

for i in range(9):
    for j in range(9):
        if board[i][j] == '.':
            board[i][j] = 0
        board[i][j] = int(board[i][j])

SudokuSolver.sudokuSolver(board)

print(board)

'''[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]'''


'''[["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]'''
