import heapq


def ucs(grafo, inicio, objetivos=None):
    visitados = set()
    costos = {inicio: 0}
    padre = {inicio: None}
    frontera = []
    paso = 0

    heapq.heappush(frontera, (0, inicio))

    while frontera:
        costo_actual, nodo = heapq.heappop(frontera)
        if nodo in visitados:
            continue

        paso += 1
        visitados.add(nodo)
        print(f"Paso {paso}")
        print(f"  Nodo activo: {nodo}")
        print(f"  Costo: {costo_actual}")
        print(f"  Visitados: {sorted(visitados)}")

        if objetivos and nodo in objetivos:
            return reconstruir_camino(padre, nodo), costo_actual

        for vecino, peso in grafo.get(nodo, {}).items():
            nuevo_costo = costo_actual + peso
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                padre[vecino] = nodo
                heapq.heappush(frontera, (nuevo_costo, vecino))

        print(f"  Frontera: {sorted(frontera)}")

    return None, None


def reconstruir_camino(padre, nodo):
    camino = []
    actual = nodo
    while actual is not None:
        camino.append(actual)
        actual = padre[actual]
    camino.reverse()
    return camino


if __name__ == "__main__":
    # Grafo dirigido con pesos (aproximado al ejemplo).
    grafo = {
        "S": {"A": 5, "B": 9, "D": 6},
        "A": {"B": 3, "X": 9},
        "B": {"A": 2, "C": 1},
        "C": {"S": 6, "F": 7,"Y":5},
        "D": {"E": 2,"C":2},
        "E": {"Z": 7},
        "F": {"Z": 8, "Y": 4,"D":2},
        "X": {"Y":4},
        "Y": {},
        "Z": {},
    }

    inicio = "S"
    objetivos = {"X", "Y", "Z"}
    camino, costo = ucs(grafo, inicio, objetivos)
    print("Camino UCS:", camino)
    print("Costo UCS:", costo)

    # README (breve)
    # - UCS usa una cola de prioridad (min-heap) ordenada por costo acumulado.
    """{ en Python la implementación estándar más directa es un min-heap (heapq).
heapq mantiene el elemento con menor costo en la cima y permite push/pop en 
O(logn), que es exactamente lo que necesita UCS para extraer siempre el nodo con menor costo acumulado.}"""
    # - Un nodo se expande cuando sale de la frontera con el menor costo.
    # - visitados evita reprocesar nodos; costos guarda el mejor costo conocido.
    # - objetivos es opcional; si no se pasa, solo recorre y muestra la frontera.
