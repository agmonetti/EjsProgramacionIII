def dfs_backtracking(grafo, inicio):
    visitados = set()
    recorrido = []
    paso = 0

    def dfs(nodo, profundidad):
        nonlocal paso
        paso += 1
        indent = "  " * profundidad
        print(f"{indent}Paso {paso}")
        print(f"{indent}  Vertice: {nodo}")
        print(f"{indent}  Pila: nivel {profundidad}")

        visitados.add(nodo)
        recorrido.append(nodo)
        vecindario = grafo.get(nodo, [])
        visitados_ordenados = sorted(visitados)
        print(f"{indent}  Vecindario: {vecindario}")
        print(f"{indent}  Visitados: {visitados_ordenados}")

        for vecino in vecindario:
            if vecino not in visitados:
                dfs(vecino, profundidad + 1)

        print(f"{indent}  Retroceso: nivel {profundidad}")

    dfs(inicio, 0)
    return recorrido


if __name__ == "__main__":
    # Ejemplo de grafo como lista de adyacencia.
    grafo = {
        "1": ["2"],
        "2": ["3", "4"],
        "3": ["1","6"],
        "4": ["3", "5"],
        "5": ["6"],
        "6": ["1"],
    }

    inicio = "1"
    recorrido = dfs_backtracking(grafo, inicio)
    print("Recorrido DFS:", recorrido)
