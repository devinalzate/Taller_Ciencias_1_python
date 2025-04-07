import math
from abc import ABC, abstractmethod
from typing import List
from .Politicos import Politico


# Clase abstracta (equivalente a interfaz en Java)
class SortStrategy(ABC):
    @staticmethod
    def unir_filas(matriz: List[List['Politico']]) -> List['Politico']:
        total_elementos = sum(len(fila) for fila in matriz)
        resultado = [None] * total_elementos
        index = 0
        for fila in matriz:
            for elemento in fila:
                resultado[index] = elemento
                index += 1
        return resultado

    @staticmethod
    def convertir_a_matriz(arreglo: List['Politico'], columnas: int) -> List[List['Politico']]:
        if columnas <= 0:
            raise ValueError("El número de columnas debe ser mayor que cero.")
        
        filas = math.ceil(len(arreglo) / columnas)
        matriz = [[None for _ in range(columnas)] for _ in range(filas)]
        
        for i in range(len(arreglo)):
            fila = i // columnas
            col = i % columnas
            matriz[fila][col] = arreglo[i]
        
        return matriz

    @abstractmethod
    def ordenar_arreglo(self, politicos: List['Politico'], criterio: str) -> List['Politico']:
        pass

    @abstractmethod
    def ordenar_matriz(self, matriz: List[List['Politico']]) -> List[List['Politico']]:
        pass

    @abstractmethod
    def get_comparaciones(self) -> int:
        pass

    @abstractmethod
    def get_movimientos(self) -> int:
        pass

    @abstractmethod
    def get_tiempo_ejecucion(self) -> float:
        pass
