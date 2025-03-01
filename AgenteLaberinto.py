import random
from collections import deque

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(" ".join(fila))
    print()

def generar_laberinto():
    """Genera un laberinto 5x5 con paredes y una meta."""
    laberinto = [["-" for _ in range(5)] for _ in range(5)]
    for _ in range(5):  
        x, y = random.randint(0, 4), random.randint(0, 4)
        laberinto[x][y] = "X"
    
    meta = (random.randint(0, 4), random.randint(0, 4))
    while laberinto[meta[0]][meta[1]] == "X":
        meta = (random.randint(0, 4), random.randint(0, 4))
    laberinto[meta[0]][meta[1]] = "M"
    
    return laberinto, meta

def encontrar_camino(laberinto, inicio, meta):
    """Implementa una búsqueda de la ruta más corta usando BFS."""
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cola = deque([(inicio, [])])
    visitados = set()
    
    while cola:
        (x, y), camino = cola.popleft()
        
        if (x, y) == meta:
            return camino + [(x, y)]
        
        if (x, y) in visitados:
            continue
        visitados.add((x, y))
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and laberinto[nx][ny] != "X" and (nx, ny) not in visitados:
                cola.append(((nx, ny), camino + [(x, y)]))
    
    return []

def navegar():
    laberinto, meta = generar_laberinto()
    inicio = (0, 0)
    laberinto[inicio[0]][inicio[1]] = "A"
    imprimir_laberinto(laberinto)
    
    camino = encontrar_camino(laberinto, inicio, meta)
    if camino:
        print("Ruta encontrada:")
        for paso in camino:
            laberinto[paso[0]][paso[1]] = "."
        laberinto[inicio[0]][inicio[1]] = "A"
        laberinto[meta[0]][meta[1]] = "M"
        imprimir_laberinto(laberinto)
    else:
        print("No se encontró una ruta a la meta.")

# Ejecutar la navegación
navegar()
