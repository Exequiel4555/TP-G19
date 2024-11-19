from termcolor import colored  
from random import randint, shuffle  
from pyfiglet import Figlet  
import os  
import time

# ------------------------------------------------------- BANNER  
def Banner():  
    """Muestra el Banner principal.  
    Args:  
        None.  
    Returns:  
        Retorna el banner principal.  
    """  
    f = Figlet(font="smslant")  
    print(colored(f.renderText("SUDOKU"), "blue"))  

# ------------------------------------------------------- MATRIZ  
def Tablero():  
    """Genera tablero.  
    Args:  
        None.  
    Returns:  
        Retorna el tablero 9x9.  
    """  
    tablero = [[0] * 9 for _ in range(9)]  
    Resolver(tablero)  
    Cambiar_valores(tablero)  
    return tablero  

def Mostrar_tablero(matriz):  
    """Muestra el tablero en pantalla.  
    Args:  
        Tablero.  
    Returns:  
       None.  
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
    """Resuelve el tablero.  
    Args:  
        Tablero.  
    Returns:  
       None.  
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
    """Verifica el tablero si esta correctamente.  
    Args:  
        Tablero.  
        Fila.  
        Columna.  
        Num(es el numero de la lista numeros).  
    Returns:  
       True(es valido por que verifica si no hay ningun numero repetido en la fila,columna y subcuadro 3x3).  
    """  
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

def Cambiar_valores(tablero, vaciar=2):  
    """Remueve números del tablero para crear un rompecabezas con la cantidad deseada de celdas vacías.  
    Args:  
        Tablero.  
        Vaciar(genera un espacio).  
    Returns:  
       Tablero.  
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
    """Verifica si el tablero está completo.  
    Args:  
        Tablero.  
        Vaciar(genera un espacio o input).  
    Returns:  
       Tablero.  
    """  
    for fila in tablero:  
        if 0 in fila:  
            return False  
    return True  

# -------------------------------------------------------------- INPUTS Y VALIDACIONES  
def posicion_num(tablero):   
    while True:    
        fila = int(input("[+] Ingresar Fila (1-9) : ")) - 1  
        columna = int(input("[+] Ingresar Columna (1-9): ")) - 1  

        if 0 <= fila < 9 and 0 <= columna < 9:  
            if tablero[fila][columna] == 0:  
                return fila, columna  
            else:  
                print(colored("[!] Posición ya ocupada. Intenta de nuevo.", "red"))  
        else:  
            print(colored("[!] Fila o columna fuera de rango. Deben ser entre 1 y 9.", "red"))  

def insert_num(tablero, num, fila, columna):  
    """Intenta insertar un número en el tablero en la posición dada.  
    Args:  
        Tablero.  
        Num.  
        Fila.  
        Columna.  
    Returns:  
       True(Si el numero ingresado es correcto).  
       False(Si el numero ingresado es incorrecto).  
    """  
    if es_valido(tablero, fila, columna, num):  
        tablero[fila][columna] = num  
        return True  
    return False  

def Seleccion_numero():  
    """Solicita al usuario un número entre 1 y 9.  
    Args:  
        None  
    Returns:  
       True(Si el numero ingresado es correcto).  
    """  
    while True:  
        try:  
            num = int(input("[+] Ingresar Número (1-9): "))  
            if 1 <= num <= 9 or num == -99:  
                return num  
            else:  
                print(colored("[!] Número inválido. Debe ser entre 1 y 9.", "red"))  
        except ValueError:  
            print(colored("[!] Entrada inválida. Por favor, ingresa un número entre 1 y 9.", "red"))  
#------------------------------------------------------------ARCHIVO
def guardar_puntuacion(usuario, tiempo, puntos):  
    """Guarda el nombre de usuario y el tiempo en un archivo txt."""  
    with open('puntuaciones.txt', 'a') as archivo:  
        archivo.write(f'Usuario: {usuario}, Tiempo: {tiempo:.2f} segundos Ptos: {puntos}\n') 
#------------------------------------------------------------------PISTAS
def completar_numero(tablero):
    """Completa automáticamente un número válido en el tablero en la primera celda vacía encontrada.
    
    Args:
        tablero: La matriz 9x9 del Sudoku.

    Returns:
        bool: True si se completó un número, False si no hay celdas vacías.
    """
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:  
                for num in range(1, 10):  
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        print(colored(f"[+] Número {num} completado automáticamente en la posición ({fila + 1}, {columna + 1}).", "green"))
                        return True
    return False  

#-----------------------------------------------------------DIFICULTAD_NORMAL  
def Dificultad_normal(tablero, usuario):
    """Realiza una partida de Sudoku en modo normal."""
    start_time = time.time()
    error = 0
    puntos = 1000

    while not tablero_completo(tablero):  
        Mostrar_tablero(tablero)  
        numero = Seleccion_numero()  

        if numero == -99:  
            if completar_numero(tablero):  
                puntos -= 20  
            continue

        fila, columna = posicion_num(tablero)  

        if not insert_num(tablero, numero, fila, columna):  
            error += 1
            puntos -= 50
            print(colored(f"[!] ERROR: Número {numero} no válido en ({fila + 1}, {columna + 1}).", "red"))
            if error >= 3:
                print(colored("[!] Has alcanzado el límite de 3 errores. Juego terminado.", "red"))
                main()  
                return

    end_time = time.time()
    total_time = end_time - start_time
    puntos -= int(total_time // 10) 

    Mostrar_tablero(tablero)
    print(colored("[+] ¡Felicidades! Has completado el Sudoku correctamente.", "green"))
    print(colored(f"Tiempo total jugado: {total_time:.2f} segundos", "yellow"))
    print(colored(f"Puntaje final: {max(0, puntos)} puntos", "magenta"))
    guardar_puntuacion(usuario, total_time, puntos)
    main()



#--------------------------------------------------------------DIFICULTAD_EXTREMA  
def Dificultad_extremo(tablero):  
    '''PARTIDA DIFICULTAD EXTREMA.  
    Args:  
      Tablero  
    Returns:  
       None  
    '''
    try:   
        while True:  
            Mostrar_tablero(tablero)  
            numero = Seleccion_numero()  
            Fila, Columna = posicion_num(tablero)  
            if not insert_num(tablero, numero, Fila, Columna):  
                lista = listar_archivos()   
                borrar_archivos(lista)  
            Mostrar_tablero(tablero)  
            tablero_completo(tablero)  
            numero = Seleccion_numero()  
    except (IndexError, ValueError, TypeError):  
        print(colored("[!] Indice fuera de rango", "red"))  

listar_archivos = lambda: list(filter(os.path.isfile, os.listdir('.')))   

def borrar_archivos(lista):  
    """Borrar el primer archivo de la lista proporcionda.  
    Args:  
       Lista  
    Returns:  
       None  
    """  
    if not lista:  
        print(colored("[!] No hay archivos para borrar.", "yellow"))  
        return  
    nombre_archivo = lista[0]  
    try:         
        os.remove(nombre_archivo)  
        print(colored(f"[!] El archivo '{nombre_archivo}' ha sido borrado.", "red"))  
    except OSError as e:  
        print(colored(f"[!] Error al borrar el archivo '{nombre_archivo}': {e}", "red"))  

#---------------------------------------------------------- MENÚ DE OPCIONES  
def Mostrar_inicio():  
    """Muestra las opciones iniciales del juego y retorna la elección del usuario.  
    Args:  
       None  
    Returns:  
       Choice(las opciones a elegir del menu)  
    """  
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
    """Muestra los modos de dificultad y retorna la elección del usuario.  
    Args:  
       None  
    Returns:  
       Modo(las opciones a elegir del modo de juego)  
    """   
    modos = {  
        1: "Normal",  
        2: "Extremo",  
        3: "Regresar al Menú Principal"  
    }  
    print(colored("\n===== SELECCIONA DIFICULTAD =====", "magenta"))  
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

#---------------------------------------------------------------- INTRUCCIONES  
def Mostrar_Instrucciones():  
    """Muesta las instruccion del juego.   
    Args:  
       None  
    Returns:  
       Instrucciones  
    """   
    instrucciones = """  
El objetivo del Sudoku es llenar todas las celdas vacías en un tablero de orden 9 de manera que:  

- Cada fila contenga todos los numeros del 1 al 9 sin repetir ninguno.  
- Cada columna contenga todos los números del 1 al 9 sin repetir ninguno.  
- Cada una de las nueve subcuadriculas de 3x3 contengan todos los números del 1 al 9 sin repetir ninguno.  

¡Buena suerte!   
"""  
    print(colored(instrucciones, "green"))  

# ----------------------------------------------------------------INICIO DEL JUEGO  
def Inicio():  
    """Gestiona la elección inicial del usuario """
    while True:
        try:   
            Continuar = True  
            while Continuar:
                usuario = input("[!] Ingresar usuario: ") 
                choice = Mostrar_inicio()  
                if choice == 1:  
                    while True:  
                        modo = Mostrar_Modo()  
                        if modo == 1:  
                            tablero = Tablero()  
                            Dificultad_normal(tablero,usuario)  
                        elif modo == 2:  
                            tablero = Tablero()   
                            Dificultad_extremo(tablero)  
                        elif modo == 3:  
                            main()   
                elif choice == 2:  
                    Mostrar_Instrucciones()  
                elif choice == 3:  
                    Continuar = False  
        except KeyboardInterrupt as e:  
            print(e)  
        finally:  
            print(colored("\n[+] ¡Gracias por jugar Sudoku! Hasta la próxima.", "cyan"))  

# ------------------------------------------------------- PROGRAMA PRINCIPAL  
def main():  
    Banner()  
    Inicio()  

if __name__ == "__main__":  
    main()
