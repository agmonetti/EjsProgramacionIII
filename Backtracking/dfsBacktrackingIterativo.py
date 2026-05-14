def dfs_iterativo(grafo, inicio):
    visitados = set()
    recorrido = []
    pila = []
    paso = 0

    # Si va a la pila, debe ir a visitados.
    pila.append(inicio)
    visitados.add(inicio)

    while pila:
        paso += 1
        vertice = pila.pop()

        print(f"Paso {paso}")
        print(f"  Vertice: {vertice}")
        print(f"  Pila: {pila}")

        recorrido.append(vertice)
        vecindario = grafo.get(vertice, set())
        visitados_ordenados = sorted(visitados)
        print(f"  Vecindario: {sorted(vecindario)}")
        print(f"  Visitados: {visitados_ordenados}")

        # Apilar primero, luego marcar visitado (como en el pseudocodigo).
        for vecino in sorted(vecindario, reverse=True):
            if vecino not in visitados:
                pila.append(vecino)
                visitados.add(vecino)

    return recorrido


if __name__ == "__main__":
    # Ejemplo de grafo como lista de adyacencia.
    grafo = {
        "1": {"2"},
        "2": {"3", "4"},
        "3": {"1", "6"},
        "4": {"3", "5"},
        "5": {"6"},
        "6": {"1"},
    }

    inicio = "1"
    recorrido = dfs_iterativo(grafo, inicio)
    print("Recorrido DFS (iterativo):", recorrido)
