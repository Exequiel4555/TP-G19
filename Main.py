from termcolor import colored
from random import randint,shuffle
from pyfiglet import Figlet


# ------------------------------------------------------- DiSeÑOs
def print_Baner():
    f = Figlet(font="smslant")
    print(f.renderText("SUDOKU"))


# ------------------------------------------------------- mAtRiZ
def GenerarMatriz():
    tablero = [[0] * 9 for _ in range(9)]
    return tablero


def MatrizxPantalla(matriz):
    """MUESTRA MATRIZ POR PANTALLA"""
    print("\n")
    for f in range(9):
        for c in range(9):
            print("%3d" %matriz[f][c], end=" ")
        print()


def resolver(tablero):
    """RESUELVE TABLERO"""
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
    """INSERTAR VALORES 0"""
    orden = len(tablero)
    for f in range(orden):
        for c in range(orden):
            if randint(0, 1):
                tablero[f][c] = 0
    return tablero


# -----------------------------------------------------------------# MoDo
def posicion_num(tablero):
    """VERIFICAR QUE EXISTA UNA POSICION VACIA EN EL TABLERO"""
    fila = int(input("[+] Ingresar Fila: "))
    columna = int(input("[+] Ingresar Columna:"))
    while tablero[fila][columna] != 0:
        print(colored("\n[!] POSICION INVALIDA", "red"))
        fila = int(input("[+] Ingresar Fila: "))
        columna = int(input("[+] Ingresar Columna:"))
    return fila, columna


def insert_num(tablero, num, fila, columna):
    """VERIFICAR QUE NO SE REPITA EN LA FILA Y COLUMNA"""
    error = 0
    if num in tablero[fila]:
        error += 1
        return print(colored(f"[!] ERROR:{error}", "red"))
    for i in range(9):
        if tablero[i][columna] == num:
            error += 1
            return print(colored(f"[!] ERROR:{error}", "red"))
    tablero[fila][columna] = num
    return tablero


def check_num():
    num = int(input("[+] Ingresar Numero: "))
    while num < 1 or num > 9:
        print(colored("[!] Numero invalido\n", "red"))
        num = int(input("[+] Ingresar Numero: "))
    return num


def Nueva_Partida():
    """TABLERO NUEVA PARTIDA"""
    try:
        tablero = GenerarMatriz()
        resolver(tablero)
        BorrarValores(tablero)
        MatrizxPantalla(tablero)
        num = check_num()
        while True:
            fila, columna = posicion_num(tablero)
            insert_num(tablero, num, fila, columna)
            MatrizxPantalla(tablero)
            num = check_num()
    except IndexError:
        print(colored("[!] Indice fuera de rango","red"))


# ----------------------------------------------------------------#PaRtidA
def partida():
    """ELECCION DE MODO"""
    diccionario = {1: "Nueva Partida", 2: "Instrucciones"}
    for i, j in diccionario.items():
        print(i, j)
    choice = int(input("[+] Ingresar modo: "))
    if choice == 1:
        Nueva_Partida()

    if choice == 2:
        print(
            colored(
                "\nEl objetivo del Sudoku es llenar todas las celdas vacías en un tablero de 9x9 de manera que cada fila,\ncada columna y cada una de las nueve subcuadrículas de 3x3 contenga todos los números del 1 al 9 sin repetir ninguno.\n",
                "green",
            )
        )
        partida()
    return diccionario

    # def modo():
    modo = {1: "Facil", 2: "Medio", 3: "Dificil"}

    print(modo[1])
    print(modo[2])
    print(modo[3])
    dificultad = int(input("[+] Ingresar dificultad"))
    return dificultad


# -----------------------------------------------------------------# MaIn
def main():
    try:
        print_Baner()
        partida()
    except (ValueError,TypeError,KeyboardInterrupt):
        print(colored("[!] Error Inesperado","red"))


if __name__ == "__main__":
    main()
