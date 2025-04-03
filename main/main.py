import algoritmos_arreglos, algortimos_matriz

n = int(input("ingrese una cantidad de politicos: "))

lista = algoritmos_arreglos.CreateList(n)

algoritmos_arreglos.PrintList(lista)


matriz = algortimos_matriz.CreateMatriz(lista)
algortimos_matriz.imprimir_matriz_politicos(matriz)
algortimos_matriz.SortBubbleMatriz(matriz)