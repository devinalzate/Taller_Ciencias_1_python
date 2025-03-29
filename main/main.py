import algoritmos_arreglos

n = int(input("ingrese una cantidad de politicos: "))

list = algoritmos_arreglos.CreateList(n)

algoritmos_arreglos.PrintList(list)
lista_ordenada = algoritmos_arreglos.SortInsertPoliticos(list)
print("LISTA ORDENADA CON INSERT")
algoritmos_arreglos.PrintList(lista_ordenada)