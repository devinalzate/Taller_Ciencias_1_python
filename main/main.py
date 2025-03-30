import algoritmos_arreglos

n = int(input("ingrese una cantidad de politicos: "))

list = algoritmos_arreglos.CreateList(n)

algoritmos_arreglos.PrintList(list)

print("\nLISTA ORDENADA CON INSERT\n")
algoritmos_arreglos.SortInsertPoliticos(list)
# lista_ordenada_burbuja = algoritmos_arreglos.SortBubblePoliticos(list)
# print("\nLISTA ORDENADA CON BUBBLE\n")
# algoritmos_arreglos.PrintList(lista_ordenada_burbuja)