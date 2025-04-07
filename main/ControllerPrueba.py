
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import random
import math
from typing import List
from models.BubbleSortStrategy import BubbleSortStrategy
from models.InsertSortStrategy import InsertionSortStrategy
from models.MergeSortStrategy import MergeSortStrategy
from models.Politicos import Politico
from models.QuickSortStrategy import QuickSortStrategy
from models.SelectionSortStrategy import SelectionSortStrategy




class ControllerPrueba:
    def __init__(self):
        self.insert = InsertionSortStrategy()
        self.bubble = BubbleSortStrategy()
        self.merge = MergeSortStrategy()
        self.selection = SelectionSortStrategy()
        self.quick = QuickSortStrategy()

    def iniciar_ordenamiento_arreglo(self, metodo: str, n: int):
        lista = self.create_array_politicos(n)
        self.print_politicos(lista)

        if metodo == "insert":
            lista_ordenada = self.insert.ordenar_arreglo(lista, "dinero")
        elif metodo == "merge":
            lista_ordenada = self.merge.ordenar_arreglo(lista, "dinero")
        elif metodo == "bubble":
            lista_ordenada = self.bubble.ordenar_arreglo(lista, "dinero")
        elif metodo == "selection":
            lista_ordenada = self.selection.ordenar_arreglo(lista, "dinero")
        elif metodo == "quick":
            lista_ordenada = self.quick.ordenar_arreglo(lista, "dinero")
        else:
            raise ValueError("Método no válido")

        self.print_politicos(lista_ordenada)

    def iniciar_ordenamiento_matriz(self, metodo: str, n: int):
        lista = self.create_array_politicos(n)
        matriz = self.create_matriz(lista)
        self.imprimir_matriz_politicos(matriz)

        if metodo == "insert":
            matriz_ordenada = self.insert.ordenar_matriz(matriz)
        elif metodo == "merge":
            matriz_ordenada = self.merge.ordenar_matriz(matriz)
        elif metodo == "bubble":
            matriz_ordenada = self.bubble.ordenar_matriz(matriz)
        elif metodo == "selection":
            matriz_ordenada = self.selection.ordenar_matriz(matriz)
        elif metodo == "quick":
            matriz_ordenada = self.quick.ordenar_matriz(matriz)
        else:
            raise ValueError("Método no válido")

        self.imprimir_matriz_politicos(matriz_ordenada)

    def create_array_politicos(self, n: int) -> List[Politico]:
        politicos = []
        for i in range(n):
            politico = Politico()
            politico.id = i
            politico.edad = random.randint(20, 60)
            politico.valor_robo = random.randint(1, 1000001)
            politicos.append(politico)
        return politicos

    def print_politicos(self, politicos: List[Politico]):
        for politico in politicos:
            print(f"Politico de id: {politico.id}")
            print(f"Roba una cantidad de: {politico.valor_robo}")
            print(f"Tiene una edad de: {politico.edad}")
            print("---------------------------------------------")
            print("---------------------------------------------")
            print("---------------------------------------------")

    def create_matriz(self, politicos: List[Politico]) -> List[List[Politico]]:
        if not politicos:
            return [[]]

        size = len(politicos)
        min_filas = 3
        matriz_politicos = None

        for i in range(max(min_filas, math.ceil(math.sqrt(size))), min_filas - 1, -1):
            if size % i == 0:
                rows = i
                cols = size // i
                matriz_politicos = [[None for _ in range(cols)] for _ in range(rows)]
                break

        if matriz_politicos is None:
            rows = min_filas
            cols = math.ceil(size / rows)
            matriz_politicos = [[None for _ in range(cols)] for _ in range(rows)]

        index = 0
        for i in range(len(matriz_politicos)):
            for j in range(len(matriz_politicos[i])):
                if index < size:
                    matriz_politicos[i][j] = politicos[index]
                    index += 1

        return matriz_politicos

    def imprimir_matriz_politicos(self, matriz_politicos: List[List[Politico]]):
        if not matriz_politicos or not matriz_politicos[0]:
            print("╔════════════════════════════╗")
            print("║  MATRIZ VACÍA O NULA       ║")
            print("╚════════════════════════════╝")
            return

        BORDE_HORIZONTAL = "═"
        ESQUINA_SUP_IZQ = "╔"
        ESQUINA_SUP_DER = "╗"
        ESQUINA_INF_IZQ = "╚"
        ESQUINA_INF_DER = "╝"
        UNION_IZQ = "╠"
        UNION_DER = "╣"
        UNION_CENTRO = "╬"
        LINEA_VERTICAL = "║"
        SEPARADOR_HORIZONTAL = "═"

        anchos_columnas = [len("Col X") for _ in range(len(matriz_politicos[0]))]
        
        for col in range(len(matriz_politicos[0])):
            for fila in range(len(matriz_politicos)):
                if matriz_politicos[fila][col] is not None:
                    contenido = f"{matriz_politicos[fila][col].id}|{matriz_politicos[fila][col].edad}|{matriz_politicos[fila][col].valor_robo}"
                    anchos_columnas[col] = max(anchos_columnas[col], len(contenido))
            anchos_columnas[col] += 2

        print(ESQUINA_SUP_IZQ, end="")
        for col in range(len(matriz_politicos[0])):
            print(BORDE_HORIZONTAL * anchos_columnas[col], end="")
            if col < len(matriz_politicos[0]) - 1:
                print(UNION_CENTRO, end="")
        print(ESQUINA_SUP_DER)

        print(LINEA_VERTICAL, end="")
        for col in range(len(matriz_politicos[0])):
            print(f" {'Col ' + str(col):<{anchos_columnas[col]-1}}", end=LINEA_VERTICAL)
        print()

        print(UNION_IZQ, end="")
        for col in range(len(matriz_politicos[0])):
            print(SEPARADOR_HORIZONTAL * anchos_columnas[col], end="")
            if col < len(matriz_politicos[0]) - 1:
                print(UNION_CENTRO, end="")
        print(UNION_DER)

        for fila in range(len(matriz_politicos)):
            print(LINEA_VERTICAL, end="")
            for col in range(len(matriz_politicos[fila])):
                politico = matriz_politicos[fila][col]
                contenido = f"{politico.id}|{politico.edad}|{politico.valor_robo}" if politico is not None else "null"
                print(f" {contenido:<{anchos_columnas[col]-1}}", end=LINEA_VERTICAL)
            print()

            if fila < len(matriz_politicos) - 1:
                print(UNION_IZQ, end="")
                for col in range(len(matriz_politicos[fila])):
                    print(SEPARADOR_HORIZONTAL * anchos_columnas[col], end="")
                    if col < len(matriz_politicos[fila]) - 1:
                        print(UNION_CENTRO, end="")
                print(UNION_DER)

        print(ESQUINA_INF_IZQ, end="")
        for col in range(len(matriz_politicos[0])):
            print(BORDE_HORIZONTAL * anchos_columnas[col], end="")
            if col < len(matriz_politicos[0]) - 1:
                print(UNION_CENTRO, end="")
        print(ESQUINA_INF_DER)