import time
from typing import List
from .Politicos import Politico
from .SortStrategy import SortStrategy


class InsertionSortStrategy(SortStrategy):
    def __init__(self):
        self._comparaciones = 0
        self._movimientos = 0
        self._tiempo_ejecucion = 0

    def ordenar_arreglo(self, politicos: List['Politico'], criterio: str) -> List['Politico']:
        inicio = time.time()
        copia = politicos.copy()
        self._comparaciones = 0
        self._movimientos = 0

        if criterio == "dinero":
            for i in range(1, len(copia)):
                actual = copia[i]
                j = i - 1
                self._movimientos += 1

                if actual is None:
                    break

                while j >= 0 and (copia[j].valor_robo > actual.valor_robo):
                    copia[j + 1] = copia[j]
                    j -= 1
                    self._comparaciones += 1
                copia[j + 1] = actual

        elif criterio == "edad":
            for i in range(1, len(copia)):
                actual = copia[i]
                j = i - 1
                self._movimientos += 1

                if actual is None:
                    break

                while j >= 0 and (copia[j].edad > actual.edad):
                    copia[j + 1] = copia[j]
                    j -= 1
                    self._comparaciones += 1
                copia[j + 1] = actual

        self._tiempo_ejecucion = time.time() - inicio
        return copia

    def ordenar_matriz(self, matriz: List[List['Politico']]) -> List[List['Politico']]:
        inicio = time.time()
        matriz_copia = [fila.copy() for fila in matriz]
        self._comparaciones = 0
        self._movimientos = 0

        arreglo = self.unir_filas(matriz_copia)
        arreglo_ordenado = self.ordenar_arreglo(arreglo, "edad")
        matriz_copia = self.convertir_a_matriz(arreglo_ordenado, len(matriz[0]))

        filas = len(matriz_copia)
        columnas = len(matriz_copia[0])
        max_dimension = max(filas, columnas)

        for i in range(max_dimension):
            if i < filas:
                for j in range(1, columnas):
                    politico = matriz_copia[i][j]
                    k = j - 1

                    if politico is None:
                        break

                    while k >= 0 and matriz_copia[i][k].valor_robo > politico.valor_robo:
                        matriz_copia[i][k + 1] = matriz_copia[i][k]
                        k -= 1
                    matriz_copia[i][k + 1] = politico

        self._tiempo_ejecucion = time.time() - inicio
        return matriz_copia

    def get_comparaciones(self) -> int:
        return self._comparaciones

    def get_movimientos(self) -> int:
        return self._movimientos

    def get_tiempo_ejecucion(self) -> float:
        return self._tiempo_ejecucion