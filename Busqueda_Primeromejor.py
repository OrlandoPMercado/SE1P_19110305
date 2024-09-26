def busqueda_voraz(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para almacenar los nodos visitados
    cola = [(inicio, [inicio], 0)]  # Lista de prioridad para almacenar los nodos, el camino seguido hasta el momento y sus costos

    while cola:
        nodo_actual, camino_actual, costo_actual = cola.pop(0)  # Tomamos el primer elemento de la lista
        if nodo_actual == objetivo:
            print("Objetivo alcanzado:", nodo_actual)
            print("Camino seguido:", " -> ".join(camino_actual))
            return True
        if nodo_actual not in visitados:
            print("Visitando nodo:", nodo_actual)
            visitados.add(nodo_actual)
            # Agregamos los nodos vecinos, el camino y sus costos a la cola
            vecinos = grafo[nodo_actual]
            vecinos.sort(key=lambda x: x[1])  # Ordenamos los vecinos por sus costos
            for vecino, costo in vecinos:
                if vecino not in visitados:
                    cola.append((vecino, camino_actual + [vecino], costo))
    print("No se encontró el objetivo.")
    return False

# Grafo que representa una casa
grafo = {
    'Entrada': [('Cochera', 7), ('Primera sala', 5), ('Cuarto', 3)],
    'Cochera': [('Patio', 4), ('Comedor', 6), ('Escaleras', 3)],
    'Primera sala': [('Escaleras', 3)],
    'Cuarto': [('Segunda sala', 2), ('Cocina', 5)],
    'Patio': [('Refrigerador', 9)],
    'Comedor': [('Escaleras', 3), ('Refrigerador', 4)],
    'Escaleras': [('Refrigerador', 7)],
    'Segunda sala': [('Refrigerador', 1)],
    'Cocina': [('Refrigerador', 8)],
    'Refrigerador': []  # Nodo objetivo
}

# Llamamos a la función de búsqueda con el nodo de inicio 'Entrada' y el nodo objetivo 'Refrigerador'
busqueda_voraz(grafo, 'Entrada', 'Refrigerador')
