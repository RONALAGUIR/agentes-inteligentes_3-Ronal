import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

def generar_obstaculos(tablero, cantidad):
    """Coloca una cantidad específica de obstáculos en posiciones aleatorias."""
    for _ in range(cantidad):
        while True:
            x, y = random.randint(0, 4), random.randint(0, 4)
            if tablero[x][y] == "-":
                tablero[x][y] = "X"
                break

def mover_agente(agente, direccion):
    """Calcula la nueva posición del agente según la dirección."""
    x, y = agente
    if direccion == "arriba":
        return (x - 1, y) if x > 0 else agente
    elif direccion == "abajo":
        return (x + 1, y) if x < 4 else agente
    elif direccion == "izquierda":
        return (x, y - 1) if y > 0 else agente
    elif direccion == "derecha":
        return (x, y + 1) if y < 4 else agente
    return agente

def patrullar():

    tablero = [["-" for _ in range(5)] for _ in range(5)]
    generar_obstaculos(tablero, 3)
    
    agente = (0, 0)
    direccion = "derecha"
    
    while True:

        tablero_actualizado = [["-" for _ in range(5)] for _ in range(5)]
        generar_obstaculos(tablero_actualizado, 3)
        tablero_actualizado[agente[0]][agente[1]] = "A"
        imprimir_tablero(tablero_actualizado)
        
        nueva_posicion = mover_agente(agente, direccion)
        
        if tablero[nueva_posicion[0]][nueva_posicion[1]] == "X":
            print("¡Obstáculo encontrado! Cambiando dirección aleatoriamente.")
            direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        else:
            agente = nueva_posicion
        
        print(f"Agente moviéndose a {agente} en dirección {direccion}\n")
        
        input("Presiona Enter para continuar...")

# Ejecutar la patrulla
patrullar()