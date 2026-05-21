"""Versión corta de MinMax siguiendo el pseudocódigo.

Árbol:
- Hoja: número (int/float).
- Nodo interno: lista de hijos.

Función principal: `minmax(node, is_max)`.
"""

def minmax(node, is_max=True):
    if not isinstance(node, list):
        return node

    if is_max:
        value = -float('inf')
        for child in node:
            value = max(value, minmax(child, False))
    else:
        value = float('inf')
        for child in node:
            value = min(value, minmax(child, True))

    return value


if __name__ == "__main__":
    # Ejemplos cortos para probar la función
    tree1 = [[3, 5, 2], [9, 1, 7]]
    print("tree1 minmax:", minmax(tree1, True))

    tree2 = [[[3, 12, 8], [2, 4, 6]], [[14, 5], [2, 11]]]
    print("tree2 minmax:", minmax(tree2, True))
