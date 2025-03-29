import sys
from pathlib import Path

# Añade la ruta del proyecto al PATH de Python
sys.path.append(str(Path(__file__).parent.parent))  # ← Sube dos niveles (a "taller_ciencias_1/")

from models.Politicos import Politico
import random

def CreateList(n:int) -> list:
    lista = []
    for i in range(n):
        valor_robo = random.randint(100, 1000000)
        edad = random.randint(20, 60)
        politico = Politico(i, valor_robo, edad)
        
        politico_dict = {
            "id": politico.id,
            "valor_robo": politico.valor_robo,
            "edad": politico.edad
        }
        
        lista.append(politico_dict)
    return lista

def PrintList(lista):
    print(lista)