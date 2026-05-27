from heapq import heappop, heappush


def crear_nodo(node_id, nivel, tiempo, pagado, decisiones):
    return {
        "id": node_id,
        "nivel": nivel,
        "tiempo": tiempo,
        "pagado": pagado,
        "decisiones": decisiones,
    }


def cota_optimista(nodo, tareas):
    # c = lo ya pagado + penalidades inevitables desde este nodo.
    c = nodo["pagado"]
    tiempo = nodo["tiempo"]
    i = nodo["nivel"]

    while i < len(tareas):
        dur, deadline, pen = tareas[i][1], tareas[i][2], tareas[i][3]
        if tiempo + dur <= deadline:
            tiempo += dur
        else:
            c += pen
        i += 1
    return c


def cota_pesimista(nodo, tareas):
    # u = lo ya pagado + asumir que no hago ninguna tarea restante.
    u = nodo["pagado"]
    i = nodo["nivel"]
    while i < len(tareas):
        u += tareas[i][3]
        i += 1
    return u


def es_solucion(nodo, n):
    return nodo["nivel"] == n


def generar_hijos(nodo, tareas):
    hijos = []
    i = nodo["nivel"]
    nombre, dur, deadline, pen = tareas[i]

    hijos.append(
        {
            "tipo": "HACER",
            "tarea": nombre,
            "factible": nodo["tiempo"] + dur <= deadline,
            "nuevo_tiempo": nodo["tiempo"] + dur,
            "nuevo_pagado": nodo["pagado"],
            "nuevas_decisiones": nodo["decisiones"] + [1],
        }
    )

    hijos.append(
        {
            "tipo": "NO HACER",
            "tarea": nombre,
            "factible": True,
            "nuevo_tiempo": nodo["tiempo"],
            "nuevo_pagado": nodo["pagado"] + pen,
            "nuevas_decisiones": nodo["decisiones"] + [0],
        }
    )

    return hijos


def lcbb(tareas, verbose=False):
    # Cota inicial (upper): pagar todas las penalidades.
    cota = sum(t[3] for t in tareas)
    mejor_solucion = [0] * len(tareas)

    env = []  # Entorno: cola de prioridad minima por c.
    ultimo_id = 1
    contador = 0
    raiz = crear_nodo(ultimo_id, 0, 0, 0, [])
    c_raiz = cota_optimista(raiz, tareas)
    heappush(env, (c_raiz, contador, raiz))
    contador += 1

    if verbose:
        print("Upper inicial =", cota)
        print(
            f"Nodo {raiz['id']} ACTIVO | c={c_raiz} | u={cota_pesimista(raiz, tareas)}"
        )

    while env:
        c_nodo, _, nodo = heappop(env)

        if verbose:
            print(
                f"\nExpando nodo {nodo['id']} | tiempo={nodo['tiempo']} | pagado={nodo['pagado']} | c={c_nodo} | upper={cota}"
            )

        # Si el mejor de la cola ya no mejora la cota, termino.
        if c_nodo >= cota:
            if verbose:
                print("Mato resto del arbol: c_min >= upper")
            break

        for desc in generar_hijos(nodo, tareas):
            ultimo_id += 1

            if not desc["factible"]:
                if verbose:
                    print(
                        f"Nodo {ultimo_id} INFACTIBLE | {desc['tipo']} {desc['tarea']}"
                    )
                continue

            hijo = crear_nodo(
                ultimo_id,
                nodo["nivel"] + 1,
                desc["nuevo_tiempo"],
                desc["nuevo_pagado"],
                desc["nuevas_decisiones"],
            )

            c_hijo = cota_optimista(hijo, tareas)
            u_hijo = cota_pesimista(hijo, tareas)

            if c_hijo >= cota:
                if verbose:
                    print(
                        f"Nodo {hijo['id']} MUERTO | {desc['tipo']} {desc['tarea']} | c={c_hijo} >= upper={cota}"
                    )
                continue

            # u solo se usa para actualizar la cota.
            if u_hijo < cota:
                cota = u_hijo
                mejor_solucion = hijo["decisiones"] + [0] * (len(tareas) - hijo["nivel"])
                if verbose:
                    print(
                        f"Nodo {hijo['id']} mejora upper con u={u_hijo} -> nuevo upper={cota}"
                    )

            if verbose:
                print(
                    f"Nodo {hijo['id']} generado | {desc['tipo']} {desc['tarea']} | c={c_hijo} | u={u_hijo}"
                )

            if es_solucion(hijo, len(tareas)):
                if hijo["pagado"] < cota:
                    cota = hijo["pagado"]
                    mejor_solucion = hijo["decisiones"]
                    if verbose:
                        print(
                            f"Nodo {hijo['id']} es solucion mejor -> upper={cota}"
                        )
                elif verbose:
                    print(f"Nodo {hijo['id']} es solucion, no mejora upper")
            else:
                heappush(env, (c_hijo, contador, hijo))
                contador += 1
                if verbose:
                    print(f"Nodo {hijo['id']} queda ACTIVO en la cola")

    return cota, mejor_solucion


def mostrar_plan(tareas, decision, costo):
    print("\nMejor solucion:")
    tiempo = 0
    for i, d in enumerate(decision):
        nombre, dur, deadline, pen = tareas[i]
        if d == 1:
            tiempo += dur
            print(f"- {nombre}: HACER (fin={tiempo}, deadline={deadline})")
        else:
            print(f"- {nombre}: NO HACER (penalidad={pen})")
    print("Costo minimo:", costo)


if __name__ == "__main__":
    # Ejemplo de la teoria/imagen:
    # Penalidad: [4, 11, 7, 2]
    # Deadline:  [1,  3, 2, 1]
    # Duracion:  [1,  2, 1, 1]
    tareas = [
        ("t1", 1, 1, 4),
        ("t2", 2, 3, 11),
        ("t3", 1, 2, 7),
        ("t4", 1, 1, 2),
    ]

    costo, solucion = lcbb(tareas, verbose=True)
    mostrar_plan(tareas, solucion, costo)
