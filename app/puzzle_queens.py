def puzzle_queens(size):
    reinas=[-1]*size  #Reinas inizcializadas en fila -1
    solucion= algoritmo(size,reinas,0,[])
    solucion_format=[]
    for sol in solucion:
        d={i:sol[i] for i in range(len(sol))}
        solucion_format.append(d)
    return solucion_format


"""-------------------------------------------------------------
    Funcion recursiva para encontrar las soluciones 
    Args:
        size (int): Tamaño del tablero o numero de reinas
        queens (list<int>): Configuracion actual de reinas en el tablero.
        column (int): Columna del tablero para la iteracion
        solutions (list<list<int>>): Lista de soluciones encontradas hasta el momento
    Returns:
        list<list<int>> : Lista con solucion
    -------------------------------------------------------------"""
def algoritmo(size,queens,column,solutions):
    #print(size,queens,column,solutions)
    #Ya se excedio el limite del tablero
    if column>= size:
        return solutions
    #Recorrer las filas para la columna seleccionada
    for row in range(0,size):
        if validar(queens,row,column):
            queens[column]=row
            #Si la configuracion actual ya es una solucion
            if -1 not in queens and len(queens)==size:
                solutions.append(queens)
            #Continuamos algoritmo recursivo para siguiente columna
            algoritmo(size,queens[:],column+1,solutions)
    return solutions

def validar(list,row,colum):
    """-------------------------------------------------------------
    Valida los criterios de aceptacion para colocar una nueva reina
    Args:
        list (list<int>): Lista de reinas
        row (int): Fila de la nueva reina
        colum (int): Columna de la nueva reina
    Returns:
        bool: Indica si la posicion de la nueva reina es valida
    -------------------------------------------------------------"""
    #Se encuentra en la misma fila
    if row in list:
        return False
    #Recorrer las reinas colocadas
    for i in range(0,colum):
        #Se encuentra en la misma diagonal descendente
        if (list[i]-i == row-colum or list[i]+i == row+colum):
            return False
        #Se encuentra en la misma diagonal ascendente
        if (i-colum == list[i]-row or i-colum == row-list[i]):
            return False
    #Posicion valida
    return True