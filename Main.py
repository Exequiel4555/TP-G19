from termcolor import colored
from random import randint,shuffle
from pyfiglet import Figlet
# ------------------------------------------------------- BANNER
def print_Baner():
    f = Figlet(font="smslant")
    print(f.renderText("SUDOKU"))


# ------------------------------------------------------- MATRIZ
def GenerarMatriz():
    '''TABLERO'''
    tablero = [[0] * 9 for _ in range(9)]
    return tablero


def MatrizxPantalla(matriz):
    """MUESTRA TABLERO POR PANTALLA"""
    print("\n")
    for f in range(9):
        if f % 3 == 0 and f != 0:
            print("-" * 41)  # Línea horizontal entre bloques
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")  # Línea vertical entre bloques
            print("%3d" % matriz[f][c], end=" ")
        print()
    print(" ")


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
    '''COMPLETAR TABLERO'''
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

def tablero_completo(tablero):  
    """Verifica si el tablero está completo"""  
    for fila in tablero:  
        if 0 in fila:  
            return False


# -----------------------------------------------------------------# MODO
def posicion_num(tablero):
    """VERIFICAR QUE EXISTA UNA POSICION VALIDA"""
    fila = int(input("[+] Ingresar Fila: "))-1
    columna = int(input("[+] Ingresar Columna:"))-1
    while tablero[fila][columna] != 0:
        print(colored("\n[!] POSICION INVALIDA", "red"))
        fila = int(input("[+] Ingresar Fila: "))
        columna = int(input("[+] Ingresar Columna:"))
    return fila, columna


def insert_num(tablero, num, fila, columna):
    """VERIFICAR QUE NO SE REPITA EN LA FILA Y COLUMNA"""
    if num in tablero[fila]:
        return False
        
    for i in range(9):
        if tablero[i][columna] == num:
            return False
    tablero[fila][columna] = num
    return tablero


def check_num():
    '''VALIDAR DEL 1 AL 9'''
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
        error = 0
        while True:
            fila, columna = posicion_num(tablero)
            if not insert_num(tablero, num, fila, columna):
                error+=1
                print(colored(f"[!] ERROR:{error}","red"))
                if error == 3:
                    print(colored("[!] Limite de ERRORES","red"))
                    break
            MatrizxPantalla(tablero)
            tablero_completo(tablero)
            num = check_num()
    except (IndexError,ValueError,TypeError):
        print(colored("[!] Indice fuera de rango","red"))


# ----------------------------------------------------------------#PARTIDA
def partida():
    """ELECCION DE MODO"""
    diccionario = {1: "Nueva Partida", 2: "Instrucciones", 3: "Creditos"}
    for i, j in diccionario.items():
        print(i, j)
    choice = int(input("[+] Ingresar modo: "))
    if choice == 1:
        Nueva_Partida()

    if choice == 2:
        print(
            colored(
                "\nEl objetivo de este Sudoku es en una grilla de 9x9 reemplazar los ''0'' en las grillas de 3x3 por numeros del 1 al 9,\nSin que estos se repitan entre filas y columnas de la grilla mayor\n",
                "green",
            )
        )
        print(
            colored(
                "Se le proveera al usuario una interfaz en la cual podra escribir el numero que quiere ingresar,\nEn que fila y columna quiere ingresarlo, pero hay que tener cuidado si el usuario comete un error, se le sumara a un contador de errores.\n",
                "green",
            )
        )
        print(colored("[!] ERROR: 1","red"))
        print(
            colored(
                "\nAl llegar a 3 errores finalizara la partida y habra que iniciar una nueva.\nMucha suerte y a divertirse con este programa\n",
                "green",
            )
        )
        partida()
    if choice == 3:
        print(
            colored(
                "\nProgramadores y Desarrolladores",
                "black","on_white"
            )
        )
        print(
            colored(
                "\nEzequiel Villa",
                "red",
            )
        )
        print(
            colored(
                "Nahuel Stellato",
                "green",
            )
        )
        print(
            colored(
                "Ivan Fiasche",
                "blue",
            )
        )
        print(
            colored(
                "\nEntorno de Desarrollo",
                "black","on_white",
            )
        )
        print(
            colored(
                "Python Programming Language\nVersion 3.X.X",
                "blue","on_yellow",
            )
        )
        print("\n")
        partida()
    return diccionario

# -----------------------------------------------------------------# PROGRAMA PRINCIPAL
def main():
    while True:
        try:
            print_Baner()
            partida()
        except (ValueError,TypeError,KeyboardInterrupt,KeyError):
            print(colored("[!] Error Inesperado","red"))


if __name__ == "__main__":
    main()
