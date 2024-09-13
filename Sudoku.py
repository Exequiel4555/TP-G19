from termcolor import colored
from random import randint,shuffle
from pyfiglet import Figlet

#------------------------------------------------------- DiSeÑOs
def print_Baner():
    f = Figlet(font='smslant')
    print(f.renderText('SUDOKU'))

#------------------------------------------------------- mAtRiZ
def GenerarMatriz():
    tablero = [[0] * 9 for _ in range(9)]
    return tablero

def MatrizxPantalla(matriz):
    print("\n")
    for f in range(9):
        for c in range(9):
            print("%3d" %matriz[f][c], end=" ")
        print()       

def resolver(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                numeros = list(range(1, 10))
                shuffle(numeros)  # Randomizar los números para la variabilidad
                for num in numeros:
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        if resolver(tablero):
                            return True
                        tablero[fila][columna] = 0
                return False
    return True

def es_valido(tablero, fila, columna, num):
    # Verificar fila
    if num in tablero[fila]:
        return False

    # Verificar columna
    for i in range(9):
        if tablero[i][columna] == num:
            return False

    # Verificar subcuadro 3x3
    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == num:
                return False

    return True

def BorrarValores(tablero):
    orden = len(tablero)
    for f in range(orden):
        for c in range(orden):
            if randint(0,1) == True:
                tablero[f][c] = 0
    return tablero
#-----------------------------------------------------------------# MoDo
def Nueva_Partida():
    tablero =GenerarMatriz()
    resolver(tablero)
    BorrarValores(tablero)
    MatrizxPantalla(tablero)


def Instrucciones():
    pass

#-----------------------------------------------------------------# MaIn
def main():
    try:
        print_Baner()
        modo = input(colored(f"SELECCIONAR MODO \n1)Nueva Partida\n2)Instrucciones\n","green"))
        if modo == "1":
            Nueva_Partida()

    except:
        pass


    


if __name__=="__main__":
    main()