import sys
from pathlib import Path

# Añade la ruta del proyecto al PATH de Python
sys.path.append(str(Path(__file__).parent.parent))  # ← Sube dos niveles (a "taller_ciencias_1/")

from models.Politicos import Politico
import random

def SortInsertPoliticos(politicos_base: list[Politico]) -> list[Politico]:
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
    return politicos_copia

def SortBubblePoliticos(politicos_base : list[Politico]) -> list[Politico]:
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
            if politicos_copia[actual].valor_robo > politicos_copia[actual + 1].valor_robo:
                permutation = True
                # Intercambiamos los dos elementos
                politicos_copia[actual], politicos_copia[actual + 1] = \
                politicos_copia[actual + 1],politicos_copia[actual]
                
    return politicos_copia

def CreateList(n:int) -> list:
    lista = []
    for i in range(n):
        valor_robo = random.randint(100, 1000000)
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