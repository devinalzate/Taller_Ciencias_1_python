import math
from models.Politicos import Politico


def CreateMatriz(lista: Politico) -> list[list]:
    size = len(lista)
    
    if size == 0:
        return None
    
    min_filas = 2
    
    matriz_politicos = []
    
     # Buscamos el par de factores más equilibrado que cumpla con el mínimo de filas
    for i in range(max(min_filas, int(math.ceil(math.sqrt(size)))), min_filas - 1, -1):
        
        if size % i == 0:
            rows = i
            cols = size // i
            matriz_politicos = [[None for _ in range(cols)] for _ in range(rows)]
            # Llenar la matriz con los políticos y espacios vacíos como None
            index = 0
            for i in range(len(matriz_politicos)):
                for j in range(len(matriz_politicos[i])):
                    if index < size:
                        matriz_politicos[i][j] = lista[index]
                        index += 1
                    else:
                        matriz_politicos[i][j] = "None"  # Espacios vacíos explícitos

            return matriz_politicos

    # Si no encontramos divisores que cumplan con el mínimo de filas
    if matriz_politicos is None:
        # Calculamos el número de columnas necesario para tener al menos 3 filas
        rows = min_filas
        cols = math.ceil(size / rows)
        matriz_politicos = [[None for _ in range(cols)] for _ in range(rows)]
        
        # Llenar la matriz con los políticos y espacios vacíos como None
        index = 0
        for i in range(len(matriz_politicos)):
            for j in range(len(matriz_politicos[i])):
                if index < size:
                    matriz_politicos[i][j] = lista[index]
                    index += 1
                else:
                    matriz_politicos[i][j] = None  # Espacios vacíos explícitos

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