import time
from typing import List
from .Politicos import Politico
from .SortStrategy import SortStrategy


class BubbleSortStrategy(SortStrategy):
    
    def __init__(self):
        self._comparaciones = 0
        self._movimientos = 0
        self._tiempo_ejecucion = 0

    def ordenar_arreglo(self, politicos: List['Politico'], criterio: str) -> List['Politico']:
        inicio = time.time()
        politicos_copia = politicos.copy()
        self._comparaciones = 0
        self._movimientos = 0

        if criterio == "dinero":
            for i in range(len(politicos_copia) - 1):
                for j in range(len(politicos_copia) - i - 1):
                    self._comparaciones += 1
                    if politicos_copia[j].valor_robo > politicos_copia[j + 1].valor_robo:
                        politicos_copia[j], politicos_copia[j + 1] = politicos_copia[j + 1], politicos_copia[j]
                        self._movimientos += 1

        elif criterio == "edad":
            for i in range(len(politicos_copia) - 1):
                for j in range(len(politicos_copia) - i - 1):
                    self._comparaciones += 1
                    if politicos_copia[j] is not None and politicos_copia[j + 1] is not None:
                        if politicos_copia[j].edad > politicos_copia[j + 1].edad:
                            politicos_copia[j], politicos_copia[j + 1] = politicos_copia[j + 1], politicos_copia[j]
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

        filas = len(matriz_copia)
        columnas = len(matriz_copia[0])

        for i in range(filas):
            for j in range(columnas - 1):
                for k in range(columnas - j - 1):
                    if matriz_copia[i][k] is not None and matriz_copia[i][k + 1] is not None:
                        if matriz_copia[i][k].valor_robo > matriz_copia[i][k + 1].valor_robo:
                            matriz_copia[i][k], matriz_copia[i][k + 1] = matriz_copia[i][k + 1], matriz_copia[i][k]
                            self._movimientos += 1

        self._tiempo_ejecucion = time.time() - inicio
        return matriz_copia

    def get_comparaciones(self) -> int:
        return self._comparaciones

    def get_movimientos(self) -> int:
        return self._movimientos

    def get_tiempo_ejecucion(self) -> float:
        return self._tiempo_ejecucion
