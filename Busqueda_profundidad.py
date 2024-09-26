def Busq_Prof(graph, start, goal):
    visited = set()  # Conjunto para mantener los nodos visitados
    stack = [(start, [start])]  # fila de nodos a explorar, con el nodo inicial y su camino hasta ese punto

    while stack:  # Mientras la fila no esté vacía
        node, path = stack.pop()  # Tomar el último nodo de la fila
        if node not in visited:  # Si el nodo no ha sido visitado
            visited.add(node)  # Marcar el nodo como visitado
            if node == goal:  # Si el nodo es el objetivo
                return path  # Devolver el camino hasta ese nodo
            # Extender la fila con los nodos vecinos y sus caminos
            stack.extend((neighbor, path + [neighbor]) for neighbor in graph[node])

    return None  # Si no se encuentra un camino hasta el objetivo, devolver None

# Ejemplo de uso
grafo = {
    'Colomos': ['Estanque_P', 'Jardin_M'],
    'Estanque_P': ['Colomos', 'Jardin_J', 'Caballeriza'],
    'Jardin_M': ['Colomos', 'Caballeriza'],
    'Jardin_J': ['Estanque_P'],
    'Caballeriza': ['Estanque_P', 'Jardin_M']
}

start = 'Colomos'
goal = 'Caballeriza'

caballos = Busq_Prof(grafo, start, goal)

print("Recorrido por colomos", caballos)
