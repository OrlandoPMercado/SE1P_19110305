def ao_estrella(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para almacenar los nodos visitados
    frontera = [(inicio, [inicio], 0)]  # Lista de prioridad para almacenar los nodos, el camino seguido hasta el momento y sus costos

    while frontera:
        # Seleccionamos el nodo de la frontera con el menor costo estimado
        nodo_actual, camino_actual, costo_actual = min(frontera, key=lambda x: x[2])
        frontera.remove((nodo_actual, camino_actual, costo_actual))
        
        if nodo_actual == objetivo:
            print("Objetivo alcanzado:", nodo_actual)
            print("Camino seguido:", " -> ".join(camino_actual))
            return True
        
        visitados.add(nodo_actual)
        # Expandimos el nodo actual y añadimos los nodos vecinos a la frontera
        for vecino, costo in grafo[nodo_actual]:
            if vecino not in visitados:
                nuevo_camino = camino_actual + [vecino]
                nuevo_costo = costo_actual + costo
                frontera.append((vecino, nuevo_camino, nuevo_costo))
    print("No se encontró el objetivo.")
    return False

# Grafo que representa lugares en la ciudad
grafo = {
    'Casa': [('Cafetería', 7), ('Parque', 5), ('Tienda', 8)],
    'Cafetería': [('Centro Comercial', 4), ('Supermercado', 6), ('Oficina', 3)],
    'Parque': [('Oficina', 3)],
    'Tienda': [('Restaurante', 2), ('Cine', 5)],
    'Centro Comercial': [('Casa de un Amigo', 9)],
    'Supermercado': [('Banco', 3), ('Librería', 4)],
    'Oficina': [('Museo', 7)],
    'Restaurante': [('Biblioteca', 1)],
    'Cine': [('Biblioteca', 8)],
    'Casa de un Amigo': []  # Nodo objetivo
}

# Llamamos a la función de búsqueda con el nodo de inicio 'Casa' y el nodo objetivo 'Casa de un Amigo'
ao_estrella(grafo, 'Casa', 'Casa de un Amigo')
