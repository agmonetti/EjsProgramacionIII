"""Implementación del juego de corchos (Escabio) siguiendo el pseudocódigo.

`escabio(e, n)`:
- `e` : número de corchos restantes (int >= 0)
- `n` : 1 para MAX (jugador que quiere ganar), -1 para MIN

Devuelve 1 si gana MAX desde esta posición, -1 si gana MIN.

Reglas implícitas: en cada turno un jugador puede quitar 1, 2 o 3 corchos (si hay suficientes).
"""


def escabio(e: int, n: int) -> int:
    if e == 0:
        return n

    val = -n
    for sig in range(1, min(3, e) + 1):
        child = escabio(e - sig, -n)
        if n == 1:
            val = max(val, child)
        else:
            val = min(val, child)

        # poda: si encontramos la mejor respuesta para el jugador actual
        if n * val == 1:
            break

    return val


if __name__ == "__main__":
    print("Pruebas rápidas del juego de corchos (MAX=1, MIN=-1):\n")
    print("e\tJugador que mueve -> Resultado")
    for e in range(0, 21):
        res = escabio(e, 1)  # resultado cuando mueve MAX (n=1)
        status = "GANA" if res == 1 else "PIERDE"
        print(f"{e}\t{status}")
