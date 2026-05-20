def subset_sum(v, m):
    """Genera todas las soluciones del problema Subset Sum usando backtracking.

    Args:
        v (list[int|float]): lista de valores (se asume no negativos para la poda simple).
        m (int|float): suma objetivo.

    Returns:
        list[list[int]]: lista de soluciones, cada una es una lista de 0/1 indicando inclusión.
    """
    n = len(v)
    solutions = []
    actsol = [0] * n

    def backtrack(etapa, actsum):
        if etapa == n:
            if actsum == m:
                solutions.append(actsol.copy())
            return

        # probar no tomar el elemento
        actsol[etapa] = 0
        backtrack(etapa + 1, actsum)

        # probar tomar el elemento (solo si no se pasa de m)
        actsol[etapa] = 1
        new_sum = actsum + v[etapa]
        if new_sum <= m:
            backtrack(etapa + 1, new_sum)

        actsol[etapa] = 0

    backtrack(0, 0)
    return solutions


if __name__ == "__main__":
    # ejemplo rápido
    v = [10,3,5,7,2]
    m = 15  # valor al que se quiere llegar
    sols = subset_sum(v, m)
    print(f"Valores: {v}, objetivo: {m}")
    for s in sols:
        chosen = [v[i] for i in range(len(v)) if s[i] == 1]
        print(s, "->", chosen)
