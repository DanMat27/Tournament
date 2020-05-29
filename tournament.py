###############################################
# Author: DanMat27
# Date: 29/05/2020
# File: tournament.py
# Description:
#  Genera una tabla de torneo de participantes
#  indicados por teclado de forma aleatoria.
#  Esta tabla puede ser de 8 o 4 personas.
###############################################
import sys
import random

'''
|Function: def padding(tam, c)
|Description: Crea una cadena de padding
|  con un caracter en concreto.
|Args in: 
|    tam - Tamanio del padding
|    c - Caracter a usar
|Args out:
|    pad - Padding
'''
def padding(tam, c):
    i = 0
    pad = ""
    while i<tam:
        pad += c
        i += 1
    
    return pad

'''
|Function: def draw_tournament_4(l)
|Description: Imprime por pantalla la
|  tabla del torneo de 4 participantes.
|Args in: 
|    l - Lista con los participantes
|Args out:
|    None
'''
def draw_tournament_4(l):
    tam_pad = 70 - len(l[0]) - len(l[2])
    print(l[0] + padding(tam_pad, " ") + l[2])
    print(" |" + padding(66, " ") + "|")

    print(" " + padding(23, "-") + padding(23, " ") + padding(22, "-"))
    print(padding(23, " ") + "|" + padding(23, " ") + "|")
    print(padding(23, " ") + padding(25, "-"))
    print(padding(23, " ") + "|" + padding(23, " ") + "|")
    print(" " + padding(23, "-") + padding(23, " ") + padding(22, "-"))

    tam_pad = 70 - len(l[1]) - len(l[3])
    print(" |" + padding(66, " ") + "|")
    print(l[1] + padding(tam_pad, " ") + l[3])

'''
|Function: def draw_tournament_8(l)
|Description: Imprime por pantalla la
|  tabla del torneo de 8 participantes.
|Args in: 
|    l - Lista con los participantes
|Args out:
|    None
'''
def draw_tournament_8(l):
    tam_pad = 70 - len(l[0]) - len(l[4])
    print(l[0] + padding(tam_pad, " ") + l[4])
    print(" |" + padding(66, " ") + "|")

    print(" " + padding(23, "-") + padding(23, " ") + padding(22, "-"))
    print(padding(23, " ") + "|" + padding(23, " ") + "|")
    print(l[1] + padding(23 - len(l[1]), " ") + padding(7, "-") + padding(11, " ") + padding(7, "-") + padding(22-len(l[5]), " ") + l[5])
    print(" |" + padding(21, " ") + "|" + padding(5, " ") + "|" + padding(11, " ") + "|" + padding(5, " ") + "|" + padding(20, " ") + "|")
    print(" " + padding(23, "-") + padding(5, " ") + "|" + padding(11, " ") + "|" + padding(5, " ") + padding(22, "-"))

    print(padding(29, " ") + padding(13, "-"))

    print(" " + padding(23, "-") + padding(5, " ") + "|" + padding(11, " ") + "|" + padding(5, " ") + padding(22, "-"))
    print(" |" + padding(21, " ") + "|" + padding(5, " ") + "|" + padding(11, " ") + "|" + padding(5, " ") + "|" + padding(20, " ") + "|")
    print(l[2] + padding(23 - len(l[2]), " ") + padding(7, "-") + padding(11, " ") + padding(7, "-") + padding(22-len(l[6]), " ") + l[6])
    print(padding(23, " ") + "|" + padding(23, " ") + "|")
    print(" " + padding(23, "-") + padding(23, " ") + padding(22, "-"))

    tam_pad = 70 - len(l[3]) - len(l[7])
    print(" |" + padding(66, " ") + "|")
    print(l[3] + padding(tam_pad, " ") + l[7])


'''
|Function: main
|Description: Pide al usuario que introduzca
|  uno a uno por teclado los participantes. 
|  Luego, se imprime por pantalla el torneo.
|Args in: 
|  sys.argv[1] - Numero de participantes
'''
if __name__ == '__main__':

    if len(sys.argv) != 1:
        print("########################################################################")
        print("Número de participantes elegido: " + sys.argv[1])

        if sys.argv[1] != '8' and sys.argv[1] != '4':
            print("Error. Debe elegir 8 o 4 participantes.")

        parts = int(sys.argv[1]) # Numero de participantes

        part_list = [] # Lista de participantes
        i = 0
        while i<parts:
            p = input("Participante " + str(i+1) + ": ")
            if len(p) >= 22:
                p = p[:21]
            part_list.append(p)
            i += 1
        
        # Randomizamos la lista de participantes dos veces
        random.shuffle(part_list)
        random.shuffle(part_list)
        
        # Dibujamos la tabla de torneo
        print("\nTABLA FINAL DEL TORNEO DE " + str(parts) + " PARTICIPANTES")
        if parts == 4:
            draw_tournament_4(part_list)
        else:
            draw_tournament_8(part_list)

        print("########################################################################")

    else:
        print("########################################################################")
        print("Es necesario elegir un numero de participantes.")
        print(" > python3 tournament.py N_PARTICIPANTES")
        print("Debe ser: 8 o 4")
        print("########################################################################")
