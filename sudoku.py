sudoku=[[5, 0, 0, 0, 4, 0, 0, 0, 9],
        [0, 2, 0, 0, 1, 0, 6, 8, 0],
        [0, 0, 9, 8, 7, 0, 1, 0, 0],
        [0, 0, 6, 7, 0, 0, 2, 0, 0],
        [0, 9, 0, 3, 5, 4, 0, 6, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 0, 0, 6, 0, 0, 0, 2],
        [0, 1, 4, 0, 3, 0, 0, 5, 7],
        [0, 0, 5, 0, 8, 7, 0, 0, 0]]

#generar funcion que me resuelva el sudoku por filas columnas y cuadrantes

def sudoku_solver(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1,10):
                    if (k not in sudoku[i]) and (k not in [sudoku[x][j] for x in range(9)]) and (k not in [sudoku[x][y] for x in range(3*(i//3),3*(i//3)+3) for y in range(3*(j//3),3*(j//3)+3)]):
                        sudoku[i][j] = k
                        sudoku_solver(sudoku)
                        sudoku[i][j] = 0
                return
    print(sudoku)
sudoku_solver(sudoku)