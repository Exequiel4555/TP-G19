from termcolor import colored
from random import randint, shuffle
from pyfiglet import Figlet
import os
import time
import re


# ------------------------------------------------------- BANNER
def Banner():
    """Muestra el Banner principal."""
    f = Figlet(font="smslant")
    print(colored(f.renderText("SUDOKU"), "blue"))
# ----------------------------------------------------------USUARIO
def validar_usuario():
    """  
    Valida y retorna un nombre de usuario válido.  

    Returns:  
        str: Nombre de usuario que cumple con los criterios de validación.  
            Debe contener entre 3 y 15 caracteres alfanuméricos."""
    usuario = input("Ingrese su nombre de usuario: ")
    patron_usuario = r"^[a-zA-Z0-9]{3,15}$"
    if not re.match(patron_usuario, usuario):
        print(
            colored(
                "[!] El nombre de usuario no es válido. Debe tener entre 3 y 15 caracteres y solo incluir letras y números.",
                "red",
            )
        )
        usuario = input("Ingrese su nombre de usuario: ")
    return usuario
# ------------------------------------------------------- MATRIZ
def Tablero():
    """  
    Genera un nuevo tablero de Sudoku.  

    Returns:  
        list: Una matriz 9x9 que representa el tablero de Sudoku  
              parcialmente completo y válido para jugar.  
    """
    tablero = [[0] * 9 for _ in range(9)]
    Resolver(tablero)
    Cambiar_valores(tablero)
    return tablero


def Mostrar_tablero(matriz):
    """  
    Muestra el tablero de Sudoku en la consola.  

    Args:  
        matriz (list): Una matriz 9x9 que representa el estado actual  
                      del tablero de Sudoku.  
    """
    print("\n")
    for f in range(9):
        if f % 3 == 0 and f != 0:
            print("-" * 30)
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")
            num = matriz[f][c]
            if num == 0:
                print(" . ", end="")
            else:
                print(f" {num} ", end="")
        print()
    print(" ")


def Resolver(tablero):
    """  
    Resuelve el tablero de Sudoku utilizando backtracking.  

    Args:  
        tablero (list): Matriz 9x9 que representa el tablero de Sudoku.  

    Returns:  
        bool: True si se encontró una solución, False en caso contrario.  
    """
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                numeros = list(range(1, 10))
                shuffle(numeros)
                for num in numeros:
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        if Resolver(tablero):
                            return True
                        tablero[fila][columna] = 0
                return False
    return True

def es_valido(tablero, fila, columna, num):
    """  
    Verifica si un número es válido en una posición específica del tablero.  

    Args:  
        tablero (list): Matriz 9x9 que representa el tablero de Sudoku.  
        fila (int): Índice de la fila (0-8).  
        columna (int): Índice de la columna (0-8).  
        num (int): Número a verificar (1-9).  

    Returns:  
        bool: True si el número es válido en la posición, False en caso contrario.  
    """
    if num in tablero[fila]:
        return False

    for i in range(9):
        if tablero[i][columna] == num:
            return False

    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == num:
                return False
    return True

def Cambiar_valores(tablero, vaciar=2):
    """  
    Remueve números del tablero para crear celdas vacías.  

    Args:  
        tablero (list): Matriz 9x9 que representa el tablero de Sudoku.  
        vaciar (int): Cantidad de números a remover. Por defecto es 2.  

    Returns:  
        list: Tablero modificado con celdas vacías.  
    """
    count = 0
    while count < vaciar:
        fila = randint(0, 8)
        col = randint(0, 8)
        if tablero[fila][col] != 0:
            tablero[fila][col] = 0
            count += 1
    return tablero


def tablero_completo(tablero):
    """Verifica si el tablero está completo."""
    for fila in tablero:
        if 0 in fila:
            return False
    return True
# -------------------------------------------------------------- INPUTS Y VALIDACIONES
def posicion_num(tablero):
    while True:
        try:
            fila = int(input("[+] Ingresar Fila (1-9) : ")) - 1
            if fila == -2:
                return -1, -1  # Código especial para deshacer

            columna = int(input("[+] Ingresar Columna (1-9): ")) - 1

            if 0 <= fila < 9 and 0 <= columna < 9:
                if tablero[fila][columna] == 0:
                    return fila, columna
                else:
                    print(colored("[!] Posición ya ocupada. Intenta de nuevo.", "red"))
            else:
                print(
                    colored(
                        "[!] Fila o columna fuera de rango. Deben ser entre 1 y 9.",
                        "red",
                    )
                )
        except ValueError:
            print(colored("[!] Por favor, ingresa números válidos.", "red"))


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
            if 1 <= num <= 9 or num == -99:
                return num
            else:
                print(colored("[!] Número inválido. Debe ser entre 1 y 9.", "red"))
        except ValueError:
            print(
                colored(
                    "[!] Entrada inválida. Por favor, ingresa un número entre 1 y 9.",
                    "red",
                )
            )


# ------------------------------------------------------------ARCHIVO Y PUNTUACIONES
def guardar_puntuacion(usuario, tiempo, puntos):
    """  
    Guarda la puntuación del jugador en un archivo.  

    Args:  
        usuario (str): Nombre del jugador.  
        tiempo (float): Tiempo empleado en segundos.  
        puntos (int): Puntuación obtenida.  
    """
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"Usuario: {usuario}, Tiempo: {tiempo:.2f} segundos Ptos: {puntos}\n")

def obtener_mejores_puntajes(n=3):
    """Obtiene los n mejores puntajes del archivo de puntuaciones."""
    try:
        with open("puntuaciones.txt", "r") as archivo:
            puntuaciones = []
            for linea in archivo:
                match = re.match(r"Usuario: (\w+), Tiempo: ([\d.]+) segundos Ptos: (\d+)", linea)
                if match:
                    usuario, tiempo, puntos = match.groups()
                    puntuaciones.append(
                        {
                            "usuario": usuario,
                            "tiempo": float(tiempo),
                            "puntos": int(puntos),
                        }
                    )
            return sorted(puntuaciones, key=lambda x: (-x["puntos"], x["tiempo"]))[:n]
    except FileNotFoundError:
        return []


def mostrar_mejores_puntajes():
    """Muestra una tabla con los mejores puntajes."""
    mejores = obtener_mejores_puntajes()
    if not mejores:
        print(colored("\n[!] No hay puntuaciones registradas aún.", "yellow"))
        return

    print(colored("\n===== MEJORES PUNTUACIONES =====", "blue"))
    print(colored("Pos  Usuario         Puntos    Tiempo", "cyan"))
    print(colored("-" * 40, "cyan"))

    for i, score in enumerate(mejores, 1):
        print(
            colored(
                f"{i:2d}.  {score['usuario']:<14} {score['puntos']:>7d}  {score['tiempo']:>7.2f}s",
                "green" if i == 1 else "white",
            )
        )
    print()


# ------------------------------------------------------------------PISTAS
def completar_numero(tablero):
    """Completa automáticamente un número válido en el tablero en la primera celda vacía encontrada."""
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        print(colored(f"[+] Número {num} completado automáticamente en la posición ({fila + 1}, {columna + 1}).","green"))
                        return True
    return False


# --------------------------------------------------------------MOVIMIENTO
def deshacer_movimiento(historial, tablero):
    """Deshace el último movimiento realizado por el usuario."""
    if historial:
        ult_fila, ult_col, _ = historial.pop()
        tablero[ult_fila][ult_col] = 0
        print(colored("[+] Movimiento deshecho con éxito.", "green"))
    else:
        print(colored("[!] No hay movimientos para deshacer.", "yellow"))


# -----------------------------------------------------------DIFICULTAD_NORMAL
def Dificultad_normal(tablero, usuario):
    """  
    Ejecuta una partida de Sudoku en modo normal.  

    Args:  
        tablero (list): Matriz 9x9 que representa el tablero de Sudoku.  
        usuario (str): Nombre del jugador.  

    Features:  
        - Sistema de puntuación comenzando en 1000 puntos  
        - Penalización por errores (-50 puntos)  
        - Penalización por usar pistas (-20 puntos)  
        - Penalización por tiempo (cada 10 segundos)  
        - Límite de 3 errores  
    """
    start_time = time.time()
    error = 0
    puntos = 1000
    historial = []

    while not tablero_completo(tablero):
        Mostrar_tablero(tablero)

        numero = Seleccion_numero()
        if numero == -99:
            if completar_numero(tablero):
                puntos -= 20
            continue

        fila, columna = posicion_num(tablero)
        if fila == -1 and columna == -1:
            deshacer_movimiento(historial, tablero)
            continue

        if not insert_num(tablero, numero, fila, columna):
            error += 1
            puntos -= 50
            print(colored(f"[!] ERROR: Número {numero} no válido en ({fila + 1}, {columna + 1}).","red"))
            if error >= 3:
                print(colored("[!] Has alcanzado el límite de 3 errores. Juego terminado.","red"))
                main()
                return
        else:
            historial.append((fila, columna, numero))

    end_time = time.time()
    total_time = end_time - start_time
    puntos -= int(total_time // 10)

    Mostrar_tablero(tablero)
    print(colored("[+] ¡Felicidades! Has completado el Sudoku correctamente.", "green"))
    print(colored(f"Tiempo total jugado: {total_time:.2f} segundos", "yellow"))
    print(colored(f"Puntaje final: {max(0, puntos)} puntos", "magenta"))
    guardar_puntuacion(usuario, total_time, puntos)
    main()
# --------------------------------------------------------------DIFICULTAD_EXTREMA
def Dificultad_extremo(tablero):  
    """  
    Ejecuta una partida de Sudoku en modo extremo.  

    Args:  
        tablero (list): Matriz 9x9 que representa el tablero de Sudoku.  

    Warning:  
        En este modo, cada error resulta en la eliminación de un archivo  
        del directorio actual.  
    """  
    while not tablero_completo(tablero):  
        Mostrar_tablero(tablero)  
        numero = Seleccion_numero()  
        fila, columna = posicion_num(tablero)  

        if not insert_num(tablero, numero, fila, columna):  
            lista = listar_archivos()  
            borrar_archivos(lista)  
    Mostrar_tablero(tablero)  
    print(colored("[+] ¡Felicidades! Has completado el Sudoku correctamente.", "green")) 

listar_archivos = lambda: list(filter(os.path.isfile, os.listdir(".")))

def borrar_archivos(lista):
    """Borrar el primer archivo de la lista proporcionda."""
    if not lista:
        print(colored("[!] No hay archivos para borrar.", "yellow"))
        return
    nombre_archivo = lista[0]
    try:
        os.remove(nombre_archivo)
        print(colored(f"[!] El archivo '{nombre_archivo}' ha sido borrado.", "red"))
    except OSError as e:
        print(colored(f"[!] Error al borrar el archivo '{nombre_archivo}': {e}", "red"))

# ---------------------------------------------------------- MENÚ DE OPCIONES
def Mostrar_inicio():
    """  
    Muestra y gestiona el menú principal del juego.  

    Returns:  
        int: Opción seleccionada por el usuario:  
            1: Nueva Partida  
            2: Instrucciones  
            3: Leaderboard  
            4: Salir  
    """
    opciones = {1: "Nueva Partida", 2: "Instrucciones", 3: "Leaderboard", 4: "Salir"}
    print("\n===== MENÚ PRINCIPAL =====")
    for clave, valor in opciones.items():
        print(f"{clave}. {valor}")

    if opciones:
        try:
            choice = int(input("[+] Ingresar opción: "))
            if choice in opciones:
                return choice
            else:
                print(
                    colored("[!] Opción inválida. Selecciona una opción válida.", "red")
                )
        except ValueError:
            print(colored("[!] Por favor, ingresa un número válido.", "red"))


def Mostrar_Modo():
    """Muestra los modos de dificultad y retorna la elección del usuario."""
    modos = {1: "Normal", 2: "Extremo", 3: "Regresar al Menú Principal"}
    print(colored("\n===== SELECCIONA DIFICULTAD =====", "magenta"))
    for clave, valor in modos.items():
        print(f"{clave}. {valor}")

    if modos:
        try:
            modo = int(input("[+] Ingresar modo: "))
            if modo >= 1 and modo <= 3:
                return modo
            else:
                print(
                    colored("[!] Modo inválido. Selecciona una opción válida.", "red")
                )

        except ValueError:
            print(colored("[!] Por favor, ingresa un número válido.", "red"))


# ---------------------------------------------------------------- INTRUCCIONES
def Mostrar_Instrucciones():
    """Muestra las instrucciones del juego."""
    instrucciones = """  
El objetivo del Sudoku es llenar todas las celdas vacías en un tablero de orden 9 de manera que:  

- Cada fila y columna contenga todos los numeros del 1 al 9 sin repetir ninguno.    
- Cada una de las nueve subcuadriculas de 3x3 contengan todos los números del 1 al 9 sin repetir ninguno.  

Instrucciones especiales:  
-------------------------
* **-99:**  En número : Completará una casilla con el valor correcto, pero restará 50 puntos de tu puntuación. Úsalo con cautela.  
* **-1:** En fila o columna : Deshará tu último movimiento.  

Sistema de puntuacion:
----------------------
Comienzas con un puntaje base de 1000 puntos.
Cada error al insertar un número restará 50 puntos de tu total.
Usar la opción de completar automáticamente restará 20 puntos.
El tiempo también afecta tu puntaje final, restando puntos por cada 10 segundos jugados.

¡Buena suerte!   
"""
    print(colored(instrucciones, "green"))


# ----------------------------------------------------------------INICIO DEL JUEGO
def Inicio():
    """Gestiona la elección inicial del usuario"""
    try:
        Continuar = 1
        while Continuar:
            usuario = validar_usuario()
            choice = Mostrar_inicio()
            if choice == 1:
                while Continuar:
                    modo = Mostrar_Modo()
                    if modo == 1:
                        tablero = Tablero()
                        Dificultad_normal(tablero, usuario)
                    elif modo == 2:
                        tablero = Tablero()
                        Dificultad_extremo(tablero)
                    if modo == 3:
                        main()  # Regresar al menú principal
            elif choice == 2:
                Mostrar_Instrucciones()
            elif choice == 3:
                mostrar_mejores_puntajes()
            elif choice == 4:
                print(colored("\n[!] Saliendo...\n", "red"))
                Continuar = 0
    except KeyboardInterrupt as e:
        print(e)
    except ValueError:
        print(colored("\nElección inváida", "red"))

# ------------------------------------------------------- PROGRAMA PRINCIPAL
def main():
    Banner()
    Inicio()


if __name__ == "__main__":
    main()
