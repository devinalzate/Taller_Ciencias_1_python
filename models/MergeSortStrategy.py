import time
from typing import List
from .Politicos import Politico
from .SortStrategy import SortStrategy

class MergeSortStrategy(SortStrategy):
    def __init__(self):
        self._comparaciones = 0
        self._movimientos = 0
        self._tiempo_ejecucion = 0

    def ordenar_arreglo(self, politicos: List['Politico'], criterio: str) -> List['Politico']:
        return self.merge_sort_politicos(politicos.copy(), 0, len(politicos) - 1, criterio)

    def ordenar_matriz(self, matriz: List[List['Politico']]) -> List[List['Politico']]:
        inicio = time.time()
        matriz_copia = [fila.copy() for fila in matriz]
        self._comparaciones = 0
        self._movimientos = 0

        arreglo = self.unir_filas(matriz_copia)
        arreglo_ordenado = self.ordenar_arreglo(arreglo, "edad")
        matriz_copia = self.convertir_a_matriz(arreglo_ordenado, len(matriz[0]))

        for i in range(len(matriz_copia)):
            matriz_copia[i] = self.merge_sort_politicos(matriz_copia[i], 0, len(matriz[i]) - 1, "dinero")

        self._tiempo_ejecucion = time.time() - inicio
        return matriz_copia

    def merge_sort_politicos(self, politicos_base: List['Politico'], izquierda: int, derecha: int, criterio: str) -> List['Politico']:
        tiempo_inicio = time.time()

        if izquierda == 0 and derecha == len(politicos_base) - 1:
            tiempo_inicio = time.time()

        if izquierda >= derecha:
            return politicos_base

        medio = izquierda + (derecha - izquierda) // 2
        self.merge_sort_politicos(politicos_base, izquierda, medio, criterio)
        self.merge_sort_politicos(politicos_base, medio + 1, derecha, criterio)
        politicos_base = self.merge_s(politicos_base, izquierda, medio, derecha, criterio)

        if izquierda == 0 and derecha == len(politicos_base) - 1:
            self._tiempo_ejecucion = time.time() - tiempo_inicio

        return politicos_base

    def merge_s(self, politicos_base: List['Politico'], izquierda: int, medio: int, derecha: int, criterio: str) -> List['Politico']:
        i = izquierda
        j = medio + 1

        while i <= medio and j <= derecha:
            if politicos_base[i] is None and politicos_base[j] is None:
                i += 1
                j += 1
                continue

            if politicos_base[i] is None:
                temp = politicos_base[j]
                k = j
                while k > i:
                    politicos_base[k] = politicos_base[k - 1]
                    k -= 1
                politicos_base[i] = temp
                self._movimientos += 1
                i += 1
                j += 1
                medio += 1
                continue

            if politicos_base[j] is None:
                j += 1
                continue

            self._comparaciones += 1
            condicion = False

            if criterio == "edad":
                condicion = politicos_base[i].edad <= politicos_base[j].edad
            elif criterio == "dinero":
                condicion = politicos_base[i].valor_robo <= politicos_base[j].valor_robo
            else:
                raise ValueError(f"Criterio no válido: {criterio}")

            if condicion:
                i += 1
            else:
                temp = politicos_base[j]
                k = j
                while k > i:
                    politicos_base[k] = politicos_base[k - 1]
                    k -= 1
                politicos_base[i] = temp
                self._movimientos += 1
                i += 1
                j += 1
                medio += 1

        return politicos_base

    def get_comparaciones(self) -> int:
        return self._comparaciones

    def get_movimientos(self) -> int:
        return self._movimientos

    def get_tiempo_ejecucion(self) -> float:
        return self._tiempo_ejecucion
