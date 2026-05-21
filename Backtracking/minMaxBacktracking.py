"""Implementación simple de MinMax (Minimax) usando backtracking/recursión.

Representación del árbol:
- Un nodo hoja es cualquier valor numérico (int/float).
- Un nodo interno es una lista de hijos, por ejemplo: [child1, child2, ...].

Funciones:
- minmax(tree, is_max=True): devuelve el valor MinMax del árbol.
- minmax_with_move(tree, is_max=True): devuelve (valor, best_index) donde best_index
  es el índice del hijo que produce ese valor (o None si hoja).

El nivel `is_max` alterna entre `True` (MAX) y `False` (MIN).
"""

from typing import Any, List, Optional, Tuple


def is_leaf(node: Any) -> bool:
    return not isinstance(node, list)


def minmax(tree: Any, is_max: bool = True) -> float:
    if is_leaf(tree):
        return tree

    if is_max:
        value = -float("inf")
        for child in tree:
            value = max(value, minmax(child, False))
        return value
    else:
        value = float("inf")
        for child in tree:
            value = min(value, minmax(child, True))
        return value


def minmax_with_move(tree: Any, is_max: bool = True) -> Tuple[float, Optional[int]]:
    if is_leaf(tree):
        return tree, None

    if is_max:
        best_val = -float("inf")
        best_idx = None
        for i, child in enumerate(tree):
            val, _ = minmax_with_move(child, False)
            if val > best_val:
                best_val = val
                best_idx = i
        return best_val, best_idx
    else:
        best_val = float("inf")
        best_idx = None
        for i, child in enumerate(tree):
            val, _ = minmax_with_move(child, True)
            if val < best_val:
                best_val = val
                best_idx = i
        return best_val, best_idx


if __name__ == "__main__":
    # Ejemplo clásico: raíz MAX con dos hijos MIN, cada MIN tiene hojas
    tree = [
        [3, 5, 2],  # MIN -> min = 2
        [9, 1, 7],  # MIN -> min = 1
    ]

    result = minmax(tree, is_max=True)
    print("Árbol:", tree)
    print("Resultado MinMax (raíz MAX):", result)

    val, move = minmax_with_move(tree, is_max=True)
    print("Valor con mejor movimiento:", val, "mejor hijo índice:", move)

    # Otro ejemplo más profundo
    tree2 = [
        [[3, 12, 8], [2, 4, 6]],  # left subtree, right subtree (both MIN level)
        [[14, 5], [2, 11]]
    ]
    print('\nÁrbol 2:', tree2)
    print('MinMax:', minmax(tree2, True))
    print('MinMax with move:', minmax_with_move(tree2, True))
