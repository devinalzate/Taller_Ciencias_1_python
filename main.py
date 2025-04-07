import sys
from pathlib import Path

from main.ControllerPrueba import ControllerPrueba
#Añade la ruta del proyecto al PATH de Python
sys.path.append(str(Path(__file__).parent.parent)) 



'''n = int(input("ingrese una cantidad de politicos: "))

lista = algoritmos_arreglos.CreateList(n)

algoritmos_arreglos.PrintList(lista)


matriz = algortimos_matriz.CreateMatriz(lista)
algortimos_matriz.imprimir_matriz_politicos(matriz)
algortimos_matriz.SortBubbleMatriz(matriz)'''


control = ControllerPrueba()
control.iniciar_ordenamiento_arreglo("merge", 10)
control.iniciar_ordenamiento_matriz("insert", 17)
control.iniciar_ordenamiento_matriz("merge", 16)
control.iniciar_ordenamiento_matriz("quick", 16)
control.iniciar_ordenamiento_matriz("selection", 16)
