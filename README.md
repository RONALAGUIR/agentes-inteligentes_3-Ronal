# agentes-inteligentes_3-Ronal
# Agentes Inteligentes

Este repositorio contiene diferentes agentes inteligentes diseñados para resolver problemas específicos mediante distintos enfoques de inteligencia artificial.

##  Problema 1: Agente de Patrullaje (Reflejo Simple)
Este agente sigue una ruta predefinida en un entorno y reacciona a la presencia de obstáculos. Si detecta un obstáculo en su camino, cambia su dirección de manera aleatoria para continuar su patrullaje sin interrupciones.

##  Problema 2: Agente Explorador de Mapas (Con Estado Interno)
El agente explora un entorno representado como una cuadrícula y recuerda las posiciones que ha visitado. Su objetivo es evitar repetir caminos y maximizar la exploración de nuevas zonas, asegurando una cobertura eficiente del área.

##  Problema 3: Agente de Navegación Autónoma (Basado en Metas)
Este agente tiene como objetivo encontrar la ruta más corta dentro de un laberinto de tamaño 5x5. Utiliza un algoritmo de búsqueda para navegar desde una posición inicial hasta la meta, evitando obstáculos y optimizando su desplazamiento.

##  Problema 4: Agente de Selección de Rutas (Basado en Utilidad)
El agente evalúa diferentes rutas en un entorno con valores de recompensa y selecciona el camino con la mayor utilidad total. Usa una función de utilidad para calcular la mejor opción y determina el recorrido óptimo en función de las recompensas acumuladas.

##  Ejecución
Cada problema cuenta con su propio script en Python. Para ejecutarlos, simplemente corre el script correspondiente en tu entorno de desarrollo.

```bash
python agente_patrujalle.py  # Para el problema 1
python agente_explorador.py   # Para el problema 2
python agente_navegacion.py   # Para el problema 3
python agente_seleccion_rutas.py  # Para el problema 4
```


