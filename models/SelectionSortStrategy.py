import time
from typing import List
from .Politicos import Politico
from .SortStrategy import SortStrategy



class SelectionSortStrategy(SortStrategy):
    def __init__(self):
        self._comparaciones = 0
        self._movimientos = 0
        self._tiempo_ejecucion = 0

    def ordenar_arreglo(self, politicos: List['Politico'], criterio: str) -> List['Politico']:
        inicio = time.time()
        politicos_copia = politicos.copy()
        self._comparaciones = 0
        self._movimientos = 0

        n = len(politicos_copia)
        
        if criterio == "dinero":
            for i in range(n - 1):
                minimo = i
                for j in range(i + 1, n):
                    self._comparaciones += 1
                    if politicos_copia[j].valor_robo < politicos_copia[minimo].valor_robo:
                        minimo = j

                if minimo != i:
                    politicos_copia[i], politicos_copia[minimo] = politicos_copia[minimo], politicos_copia[i]
                    self._movimientos += 1

        elif criterio == "edad":
            for i in range(n - 1):
                minimo = i
                for j in range(i + 1, n):
                    self._comparaciones += 1
                    if politicos_copia[j].edad < politicos_copia[minimo].edad:
                        minimo = j

                if minimo != i:
                    politicos_copia[i], politicos_copia[minimo] = politicos_copia[minimo], politicos_copia[i]
                    self._movimientos += 1

        self._tiempo_ejecucion = time.time() - inicio
        return politicos_copia

    def ordenar_matriz(self, matriz: List[List['Politico']]) -> List[List['Politico']]:
        inicio = time.time()
        matriz_copia = [fila.copy() for fila in matriz]
        self._comparaciones = 0
        self._movimientos = 0

        arreglo = self.unir_filas(matriz_copia)
        arreglo_ordenado = self.ordenar_arreglo(arreglo, "edad")
        matriz_copia = self.convertir_a_matriz(arreglo_ordenado, len(matriz[0]))

        for i in range(len(matriz_copia)):
            matriz_copia[i] = self.ordenar_arreglo(matriz_copia[i], "dinero")

        self._tiempo_ejecucion = time.time() - inicio
        return matriz_copia

    def get_comparaciones(self) -> int:
        return self._comparaciones

    def get_movimientos(self) -> int:
        return self._movimientos

    def get_tiempo_ejecucion(self) -> float:
        return self._tiempo_ejecucion
