def mochila_greedy(items, capacity):
    # items: lista de (peso, valor)
    # Ordenamos por valor/peso (de mayor a menor)
    orden = []  # (ratio, indice, peso, valor)
    for i in range(len(items)):
        valor, peso = items[i]
        ratio = valor / peso
        orden.append((ratio, i, peso, valor))
    orden.sort(reverse=True, key=lambda x: x[0])

    valor_total = 0.0
    restante = capacity
    seleccion = []  # (indice_original, fraccion_usada)

    for _, i, peso, valor in orden:
        if restante <= 0:
            break
        if peso <= restante:
            valor_total += valor
            restante -= peso
            seleccion.append((i, 1.0))
        else:
            fraccion = restante / peso
            valor_total += valor * fraccion
            seleccion.append((i, fraccion))
            restante = 0

    return valor_total, seleccion


if __name__ == "__main__":
    # valor, peso
    items = [(25,18), (24, 15), (15, 10)]
    capacidad = 20
    total, seleccion = mochila_greedy(items, capacidad)
    print(f"Valor total: {total:.2f}")
    print("Selecciones (indice, fraccion):", seleccion)
