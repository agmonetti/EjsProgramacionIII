def generar_binarios(n):
    resultado = []
    actual = [0] * n

    def backtrack(pos):
        print(f"pos={pos}, actual={actual}")
        if pos == n:
            numero = "".join(str(bit) for bit in actual)
            print(f"  -> completo: {numero}")
            resultado.append(numero)
            return

        actual[pos] = 0
        print(f"  probar 0 en pos {pos}")
        backtrack(pos + 1)

        actual[pos] = 1
        print(f"  probar 1 en pos {pos}")
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
