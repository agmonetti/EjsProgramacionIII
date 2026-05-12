# Huffman
def huffman(simbolos, frecuencias):
    # simbolos: lista de etiquetas
    # frecuencias: lista de enteros
    n = len(simbolos)

    # Cola de prioridad como lista de nodos: (frecuencia, simbolo, izq, der)
    Q = []
    for i in range(n):
        Q.append((frecuencias[i], simbolos[i], None, None))

    # Construir el arbol
    while len(Q) > 1:
        # 1) extraer minimo x
        x = extraer_min(Q)
        # 2) extraer minimo y
        y = extraer_min(Q)
        # 3) nuevo nodo z
        z = (x[0] + y[0], None, x, y)
        # 4) insertar z
        Q.append(z)

    # La raiz del arbol
    return Q[0]


def extraer_min(Q):
    # Busca el nodo con menor frecuencia
    min_i = 0
    for i in range(1, len(Q)):
        if Q[i][0] < Q[min_i][0]:
            min_i = i
    return Q.pop(min_i)


def imprimir_arbol(nodo, prefijo="", es_ultimo=True, etiqueta_rama="ROOT"):
    # Imprime el arbol con ramas ASCII y etiquetas IZQ/DER
    if nodo is None:
        return

    freq, simbolo, izq, der = nodo
    etiqueta = simbolo if simbolo is not None else "*"

    conector = "`- " if es_ultimo else "|- "
    print(f"{prefijo}{conector}[{etiqueta_rama}] {etiqueta}:{freq}")

    nuevo_prefijo = prefijo + ("   " if es_ultimo else "|  ")
    if izq is not None or der is not None:
        imprimir_arbol(izq, nuevo_prefijo, False, "IZQ (0)")
        imprimir_arbol(der, nuevo_prefijo, True, "DER (1)")


def imprimir_arbol_binario(nodo, nivel=0, lado="ROOT"):
    # Imprime el arbol de costado (estilo arbol binario)
    if nodo is None:
        return
    freq, simbolo, izq, der = nodo
    etiqueta = simbolo if simbolo is not None else "*"

    imprimir_arbol_binario(der, nivel + 1, "DER (1)")
    print("    " * nivel + f"{lado}: {etiqueta}:{freq}")
    imprimir_arbol_binario(izq, nivel + 1, "IZQ (0)")


def _construir_ascii(nodo):
    if nodo is None:
        return [""], 0, 0, 0

    freq, simbolo, izq, der = nodo
    etiqueta = simbolo if simbolo is not None else "*"
    s = f"{etiqueta}:{freq}"

    if izq is None and der is None:
        ancho = len(s)
        return [s], ancho, 1, ancho // 2

    izq_lineas, izq_ancho, izq_alto, izq_medio = _construir_ascii(izq)
    der_lineas, der_ancho, der_alto, der_medio = _construir_ascii(der)

    ancho = izq_ancho + der_ancho + 3
    medio = izq_ancho + 1

    linea_1 = (" " * medio) + s
    linea_2 = (" " * izq_medio) + "0/" + (" " * (izq_ancho - izq_medio - 1))
    linea_2 += (" " * (der_medio + 1)) + "\\1" + (" " * (der_ancho - der_medio - 2))

    altura = max(izq_alto, der_alto)
    izq_lineas += [" " * izq_ancho] * (altura - izq_alto)
    der_lineas += [" " * der_ancho] * (altura - der_alto)

    lineas = [linea_1, linea_2]
    for i in range(altura):
        lineas.append(izq_lineas[i] + "   " + der_lineas[i])

    return lineas, ancho, altura + 2, medio


def imprimir_arbol_ascii(nodo):
    # Imprime el arbol de arriba hacia abajo
    lineas, _, _, _ = _construir_ascii(nodo)
    for linea in lineas:
        print(linea.rstrip())


# Ejemplo simple
if __name__ == "__main__":
    simbolos = ["A", "B", "C", "D", "E", "F"]
    frecuencias = [45, 13, 12, 16, 9, 5]

    raiz = huffman(simbolos, frecuencias)
    print("Raiz:", raiz[0])
    imprimir_arbol_ascii(raiz)
