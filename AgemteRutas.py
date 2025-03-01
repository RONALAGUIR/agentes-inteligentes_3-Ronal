import random

def imprimir_entorno(entorno):
    for fila in entorno:
        print(" ".join(f"{celda:2}" for celda in fila))
    print()

def generar_entorno():
    """Genera un entorno 5x5 con valores de recompensa aleatorios."""
    return [[random.randint(1, 9) for _ in range(5)] for _ in range(5)]

def encontrar_mejor_ruta(entorno, inicio, meta):
    """Encuentra la ruta con la mayor utilidad usando búsqueda con función de utilidad."""
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    mejor_camino = []
    mejor_utilidad = float('-inf')
    
    def dfs(pos, camino, utilidad, visitados):
        nonlocal mejor_camino, mejor_utilidad
        
        if pos == meta:
            if utilidad > mejor_utilidad:
                mejor_utilidad = utilidad
                mejor_camino = camino[:]
            return
        
        x, y = pos
        visitados.add(pos)
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visitados:
                dfs((nx, ny), camino + [(nx, ny)], utilidad + entorno[nx][ny], visitados)
        
        visitados.remove(pos)
    
    dfs(inicio, [inicio], entorno[inicio[0]][inicio[1]], set())
    return mejor_camino

def seleccionar_ruta():
    entorno = generar_entorno()
    inicio = (0, 0)
    meta = (4, 4)
    
    print("Entorno con valores de recompensa:")
    imprimir_entorno(entorno)
    
    mejor_camino = encontrar_mejor_ruta(entorno, inicio, meta)
    
    if mejor_camino:
        print("Mejor ruta seleccionada:")
        for x, y in mejor_camino:
            entorno[x][y] = "*"
        imprimir_entorno(entorno)
        print(f"Utilidad total: {sum(entorno[x][y] if isinstance(entorno[x][y], int) else 0 for x, y in mejor_camino)}")
    else:
        print("No se encontró una ruta válida.")

# Ejecutar la selección de ruta
seleccionar_ruta()