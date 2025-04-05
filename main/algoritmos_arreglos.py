import sys, time
from pathlib import Path

# Añade la ruta del proyecto al PATH de Python
sys.path.append(str(Path(__file__).parent.parent))  # ← Sube dos niveles (a "taller_ciencias_1/")

from models.Politicos import Politico
import random

def SortInsertPoliticos(politicos_base: list[Politico]):
    inicial= time.time()
    contador_intercambios = 0
    contador_comparaciones = 0
    
    politicos_copia = politicos_base.copy()  # ¡Copia real!
    
    for i in range(1, len(politicos_copia)):
        politico = politicos_copia[i]
        j = i - 1
        while j >= 0 and politicos_copia[j].valor_robo > politico.valor_robo:
            politicos_copia[j + 1] = politicos_copia[j]
            contador_comparaciones += 1
            contador_intercambios += 1  # Cada desplazamiento cuenta como intercambio
            j -= 1  # ¡Decrementar j para evitar bucle infinito!
        politicos_copia[j + 1] = politico
    final = time.time()
    retorno = final - inicial
    
    PrintList(politicos_copia)
    print(f"demoro {retorno:.6f} segundos")

def SortBubblePoliticos(politicos_base : list[Politico]):
    inicial= time.time()
    contador_intercambios = 0
    contador_comparaciones = 0
    
    politicos_copia = politicos_base.copy()
    
    n = len(politicos_copia)
    
    permutation = True
    iteración = 0
    while permutation == True:
        permutation = False
        iteración = iteración + 1
        for actual in range(0, len(politicos_copia) - iteración):
            contador_comparaciones += 1
            if politicos_copia[actual].valor_robo > politicos_copia[actual + 1].valor_robo:
                permutation = True
                # Intercambiamos los dos elementos
                contador_intercambios += 1
                politicos_copia[actual], politicos_copia[actual + 1] = \
                politicos_copia[actual + 1],politicos_copia[actual]
    final = time.time()            
    retorno = final - inicial
    
    PrintList(politicos_copia)
    print(f"demoro {retorno:.6f} segundos")

def SortQuickPolitics(politics_base: list[Politico]):
    inicial = time.time()
    contador_intercambios = 0
    contador_comparaciones = 0
    
    politics_copia = politics_base.copy()
    
    def quick_sort(politics: list[Politico], low: int, high: int):
        nonlocal contador_intercambios, contador_comparaciones
        
        if low < high:            # Partición del array
            pivot_index = partition(politics, low, high)            # Ordenar recursivamente los subarrays
            quick_sort(politics, low, pivot_index - 1)
            quick_sort(politics, pivot_index + 1, high)
    
    def partition(politics: list[Politico], low: int, high: int) -> int:
        nonlocal contador_intercambios, contador_comparaciones
        
        pivot = politics[high].valor_robo
        i = low - 1
        
        for j in range(low, high):
            contador_comparaciones += 1
            if politics[j].valor_robo <= pivot:
                i += 1
                politics[i], politics[j] = politics[j], politics[i]                # Intercambiar elementos
                contador_intercambios += 1
        
        politics[i+1], politics[high] = politics[high], politics[i+1]        # Intercambiar el pivote con el elemento en i+1
        contador_intercambios += 1
        return i + 1
    
    quick_sort(politics_copia, 0, len(politics_copia) - 1)    # Llamar a la función principal de QuickSort
    
    final = time.time()
    retorno = final - inicial
    
    PrintList(politics_copia)
    print(f"demoro: {retorno:.6f} segundos")
    print(f"Comparaciones realizadas: {contador_comparaciones}")
    print(f"Intercambios realizados: {contador_intercambios}")

def CreateList(n:int) -> list:
    lista = []
    for i in range(n):
        valor_robo = random.randint(99, 1000001)
        edad = random.randint(20, 60)
        politico = Politico(i, valor_robo, edad)
        
        
        lista.append(politico)
    return lista

def PrintList(lista : list[Politico]):
    for i in lista:
        print("Politico de id: ",i.id, "\n", 
              "Roba una cantidad de: ", i.valor_robo, "\n", 
              "Tiene una edad de: ", i.edad)
        print("---------------------------------------------")
        print("---------------------------------------------")
        print("---------------------------------------------")