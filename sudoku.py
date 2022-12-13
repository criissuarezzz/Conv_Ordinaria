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
def print_sudoku(sudoku):
    for l in sudoku:
        print(l)

def coordenada_cuadrante(val): 
    if val <=2:         #[0,1,2] 
                        #[3,4,5] 
                        #[6,7,8]
        return 0
    elif val <=5:
        return 1
    else:
        return 2

def obtener_cuadrante(x, y, sudoku): #funcion que me da el cuadrante de la celda que le estás diciendo
    cuadrante_x= coordenada_cuadrante(x)
    cuadrante_y= coordenada_cuadrante(y)
    cuadrante= []

    for fila in sudoku[cuadrante_y*3:cuadrante_y*3+3]:
        for columna in fila[cuadrante_x*3:cuadrante_x*3+3]:
            cuadrante.append(columna)
    return cuadrante


def posible(x, y, v, sudoku):    #funcion que revisa si esa celda puede tener el valor que le estás diciendo
    #Revisar la fila
    if v in sudoku[y]:
        return False
    #Revisar la columna
    col= [fila[x] for fila in sudoku]
    if v in col:
        return False
    #Revisar cuadrantes
    cuadrante= obtener_cuadrante(x, y, sudoku)
    if v in cuadrante:
        return False
    return True




def sudoku_resolver(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for valor in range(1,10):
                    if posible(x, y, valor):
                        sudoku[y][x]= valor
                        sudoku_resolver(sudoku)
                        sudoku[y][x]= 0              
                return
    print(sudoku)

sudoku_resolver(sudoku)