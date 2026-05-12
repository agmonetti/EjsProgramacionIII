def planificar_optimizado(ganancias, tiempos):
    # 1) Ordenar por ganancia
    tareas = []  # (ganancia, plazo, indice)
    for i in range(len(ganancias)):
        tareas.append((ganancias[i], tiempos[i], i))
    tareas.sort(reverse=True, key=lambda x: x[0])

    # 2) Agenda con slots libres
    tiempo_maximo = max(tiempos) if tiempos else 0
    agenda = [-1] * tiempo_maximo

    # 3) Para cada tarea, buscar el ultimo hueco antes del plazo
    for ganancia, plazo, indice in tareas:
        for hora in range(min(tiempo_maximo, plazo) - 1, -1, -1):
            if agenda[hora] == -1:
                agenda[hora] = indice
                break

    # 4) Devolver solo las tareas asignadas
    resultado = []
    for tarea in agenda:
        if tarea != -1:
            resultado.append(tarea)
    return resultado


if __name__ == "__main__":
    ganancias = [50, 10, 15, 30]
    tiempos = [2, 1, 2, 1]

    secuencia = planificar_optimizado(ganancias, tiempos)
    secuencia_humana = [t + 1 for t in secuencia]

    print(f"Ganancias: {ganancias}")
    print(f"Tiempos limite: {tiempos}")
    print(f"Secuencia optima encontrada: {secuencia_humana}")