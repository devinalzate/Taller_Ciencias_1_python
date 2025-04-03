import math
from models.Politicos import Politico

import math

def SortInsertMatriz(lista) -> list[Politico]:
    matriz_copia = lista
    
    for i in range (0,len(matriz_copia)):
        if i < len(matriz_copia):
           for j in range(0, len(matriz_copia[0])):
                politico = matriz_copia[i][j]
                k = j - 1
                if politico == None:
                    break
                else:
                    while k >= 0 and matriz_copia[i][k].valor_robo > politico.valor_robo:
                        matriz_copia[i][k + 1] = matriz_copia[i][k]
                        k -= 1  # ¡Decrementar j para evitar bucle infinito!
                    matriz_copia[i][k + 1] = politico
                    
        if i < len(matriz_copia[0]):
            for j in range(1, len(matriz_copia)):
                politico = matriz_copia[j][i]
                k = j - 1
                if politico == None:
                    break
                else:
                    while k >= 0 and matriz_copia[k][i].edad > politico.edad:
                        matriz_copia[k+1][i] = matriz_copia[k][i]
                        k -= 1  # ¡Decrementar j para evitar bucle infinito!
                    matriz_copia[k+1][i] = politico
                    
    imprimir_matriz_politicos(matriz_copia)

def SortBubbleMatriz(lista) -> list[Politico]:
    matriz_copia = lista
    
    if not matriz_copia or not matriz_copia[0]:
        return matriz_copia
    
    rows = len(matriz_copia)
    cols = len(matriz_copia[0])
    
    # Ordenar cada fila
    for i in range(rows):
        permutation = True
        iteration = 0
        while permutation:
            permutation = False
            iteration += 1
            for j in range(0, cols - iteration):
                if matriz_copia[i][j] != None and matriz_copia[i][j + 1] != None:
                    if matriz_copia[i][j].valor_robo > matriz_copia[i][j + 1].valor_robo:
                        permutation = True
                        matriz_copia[i][j], matriz_copia[i][j + 1] = matriz_copia[i][j + 1], matriz_copia[i][j]
    
    # Ordenar cada columna
    for j in range(cols):
        permutation = True
        iteration = 0
        while permutation:
            permutation = False
            iteration += 1
            for i in range(0, rows - iteration):
                if matriz_copia[i][j] != None and matriz_copia[i + 1][j] != None:
                    if matriz_copia[i][j].edad > matriz_copia[i + 1][j].edad:
                        permutation = True
                        matriz_copia[i][j], matriz_copia[i + 1][j] = matriz_copia[i + 1][j], matriz_copia[i][j]
    imprimir_matriz_politicos(matriz_copia)
    return matriz_copia

        

def CreateMatriz(lista: list) -> list[Politico]:
    size = len(lista)
    
    if size == 0:
        return None
    
    min_filas = 4
    matriz_politicos = None
    
    # Buscamos el par de factores más equilibrado que cumpla con el mínimo de filas
    for i in range(max(min_filas, int(math.ceil(math.sqrt(size)))), min_filas - 1, -1):
        if size % i == 0:
            rows = i
            cols = size // i
            matriz_politicos = [[None for _ in range(cols)] for _ in range(rows)]
            break
    
    # Si no encontramos divisores que cumplan con el mínimo de filas
    if matriz_politicos is None:
        rows = min_filas
        cols = math.ceil(size / rows)
        matriz_politicos = [[None for _ in range(cols)] for _ in range(rows)]
    
    
    # Rellenar la matriz con los políticos y completar con None si es necesario
    index = 0
    for i in range(len(matriz_politicos)):
        for j in range(len(matriz_politicos[i])):
            if index < size:
                matriz_politicos[i][j] = lista[index]
                index += 1
            else:
                matriz_politicos[i][j] = None  # Rellenar con None si faltan elementos
    
    return matriz_politicos
    

def imprimir_matriz_politicos(matriz_politicos):
    # Validación inicial
    if matriz_politicos is None or len(matriz_politicos) == 0:
        print("╔════════════════════════════╗")
        print("║  MATRIZ VACÍA O NULA       ║")
        print("╚════════════════════════════╝")
        return

    # Constantes de formato
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

    # Calcular anchos de columnas
    anchos_columnas = [len("Col X") for _ in range(len(matriz_politicos[0]))]  # Ancho mínimo
    
    for col in range(len(matriz_politicos[0])):
        for fila in range(len(matriz_politicos)):
            if matriz_politicos[fila][col] is not None:
                contenido = f"{matriz_politicos[fila][col].id}|{matriz_politicos[fila][col].edad}|{matriz_politicos[fila][col].valor_robo}"
                anchos_columnas[col] = max(anchos_columnas[col], len(contenido))
        anchos_columnas[col] += 2  # Margen adicional

    # Imprimir encabezado superior
    print(ESQUINA_SUP_IZQ, end="")
    for col in range(len(matriz_politicos[0])):
        print(BORDE_HORIZONTAL * anchos_columnas[col], end="")
        if col < len(matriz_politicos[0]) - 1:
            print(UNION_CENTRO, end="")
    print(ESQUINA_SUP_DER)

    # Imprimir encabezado de columnas
    print(LINEA_VERTICAL, end="")
    for col in range(len(matriz_politicos[0])):
        print(f" {'Col ' + str(col):<{anchos_columnas[col]-1}}", end=LINEA_VERTICAL)
    print()

    # Imprimir separador
    print(UNION_IZQ, end="")
    for col in range(len(matriz_politicos[0])):
        print(SEPARADOR_HORIZONTAL * anchos_columnas[col], end="")
        if col < len(matriz_politicos[0]) - 1:
            print(UNION_CENTRO, end="")
    print(UNION_DER)

    # Imprimir filas de datos
    for fila in range(len(matriz_politicos)):
        print(LINEA_VERTICAL, end="")
        for col in range(len(matriz_politicos[fila])):
            politico = matriz_politicos[fila][col]
            contenido = f"{politico.id}|{politico.edad}|{politico.valor_robo}" if politico is not None else "null"
            print(f" {contenido:<{anchos_columnas[col]-1}}", end=LINEA_VERTICAL)
        print()

        # Imprimir separador entre filas (excepto después de la última)
        if fila < len(matriz_politicos) - 1:
            print(UNION_IZQ, end="")
            for col in range(len(matriz_politicos[fila])):
                print(SEPARADOR_HORIZONTAL * anchos_columnas[col], end="")
                if col < len(matriz_politicos[fila]) - 1:
                    print(UNION_CENTRO, end="")
            print(UNION_DER)

    # Imprimir borde inferior
    print(ESQUINA_INF_IZQ, end="")
    for col in range(len(matriz_politicos[0])):
        print(BORDE_HORIZONTAL * anchos_columnas[col], end="")
        if col < len(matriz_politicos[0]) - 1:
            print(UNION_CENTRO, end="")
    print(ESQUINA_INF_DER)