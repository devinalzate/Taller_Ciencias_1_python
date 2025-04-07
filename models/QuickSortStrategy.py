import time
from typing import List
from .Politicos import Politico
from .SortStrategy import SortStrategy


class QuickSortStrategy(SortStrategy):
    def __init__(self):
        self._comparaciones = 0
        self._movimientos = 0
        self._tiempo_ejecucion = 0

    def ordenar_arreglo(self, politicos: List['Politico'], criterio: str) -> List['Politico']:
        inicio = time.time()
        politicos_copia = politicos.copy()
        self._comparaciones = 0
        self._movimientos = 0

        self.quick_sort(politicos_copia, 0, len(politicos_copia) - 1, criterio)
        self._tiempo_ejecucion = time.time() - inicio
        return politicos_copia

    def quick_sort(self, arr: List['Politico'], low: int, high: int, criterio: str):
        if low < high:
            pi = self.partition(arr, low, high, criterio)
            self.quick_sort(arr, low, pi - 1, criterio)
            self.quick_sort(arr, pi + 1, high, criterio)

    def partition(self, arr: List['Politico'], low: int, high: int, criterio: str) -> int:
        i = low - 1

        if criterio == "edad":
            pivot = arr[high].edad

            for j in range(low, high):
                self._comparaciones += 1
                if arr[j].edad <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    self._movimientos += 1

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            self._movimientos += 1

        elif criterio == "dinero":
            pivot = arr[high].valor_robo

            for j in range(low, high):
                self._comparaciones += 1
                if arr[j].valor_robo <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    self._movimientos += 1

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            self._movimientos += 1

        return i + 1

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
