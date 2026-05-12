def generar_binarios(n):
    resultado = []
    actual = [0] * n

    def backtrack(pos):
        if pos == n:
            numero = "".join(str(bit) for bit in actual)
            resultado.append(numero)
            return

        actual[pos] = 0
        backtrack(pos + 1)

        actual[pos] = 1
        backtrack(pos + 1)

    backtrack(0)
    return resultado


if __name__ == "__main__":
    n = 2
    binarios = generar_binarios(n)

    # Se guarda en una lista y se imprime
    print("Lista:", binarios)
    for b in binarios:
        print(b)
