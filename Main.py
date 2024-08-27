from termcolor import colored
from random import randint


def GenerarMatriz():
    matriz = []
    for f in range(9):
        matriz.append([])
        for c in range(9):
            matriz[f].append(0)
    return matriz

def MatrizxPantalla(matriz):
    print("\n")
    for f in range(9):
        for c in range(9):
            print("%3d" %matriz[f][c], end=" ")
        print()       

def InsertarNumeros(matriz):
    for f in range(9):
        for c in range(9):
            if randint(0,1) == True:
                matriz[f][c] = randint(1,9)
    return matriz
            
#-----------------------------------------------------------------#
def Nueva_Partida():
    matriz =GenerarMatriz()

    InsertarNumeros(matriz)
    MatrizxPantalla(matriz)


def Instrucciones():
    pass

def main():
    try:
        print(colored(f"\nBIENVENIDO A SUDOKU\n","red"))
        modo = input(colored(f"Seleccionar Modo \n1)Nueva Partida\n2)Instrucciones\n","green"))
        if modo == "1":
            Nueva_Partida()

    except:
        pass


    


if __name__=="__main__":
    main()