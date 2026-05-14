from collections import deque


def bfs_backtracking(grafo, inicio):
    visitados = set()
    recorrido = []
    cola = deque()
    paso = 0

    # Si va a la cola, debe ir a visitados.
    cola.append(inicio)
    visitados.add(inicio)

    while cola:
        paso += 1
        vertice = cola.popleft()

        print(f"Paso {paso}")
        print(f"  Vertice: {vertice}")
        print(f"  Cola: {list(cola)}")

        recorrido.append(vertice)
        vecindario = grafo.get(vertice, set())
        visitados_ordenados = sorted(visitados)
        print(f"  Vecindario: {sorted(vecindario)}")
        print(f"  Visitados: {visitados_ordenados}")

        for vecino in vecindario:
            if vecino not in visitados:
                # Encolar primero, luego marcar visitado (como en el pseudocodigo).
                cola.append(vecino)
                visitados.add(vecino)

    return recorrido


if __name__ == "__main__":
    # Ejemplo aproximado basado en la imagen (sin nodo objetivo).
    grafo = {
        "S": {"A", "B", "C"},
        "A": {"B", "E","S"},
        "B": {"C", "E", "F"},
        "C": {"D", "F", "X"},
        "D": {"F", "X"},
        "E": {"F"},
        "F": {"Y","C"},
        "X": set(),
        "Y": set(),
    }

    inicio = "S"
    recorrido = bfs_backtracking(grafo, inicio)
    print("Recorrido BFS:", recorrido)

    # README 
    # - La imagen es pseudocodigo: el programa necesita estructuras reales.
    # - Q (cola) se implementa con deque para respetar el orden FIFO de BFS.
    # - visitados es un set para evitar repetir nodos y encolarlos varias veces.
    # - vecindario viene del grafo: grafo.get(vertice, set()).
    # - Los prints son solo para visualizacion; no son parte del algoritmo.
