import math

def dijkstra_simple(grafo, origen):
    # PREPARACIÓN (La tablita inicial)
    # Todos los nodos arrancan con costo Infinito, excepto el origen que vale 0
    costos = {nodo: math.inf for nodo in grafo}
    costos[origen] = 0
    
    # Conjunto para llevar registro de los que ya sacamos del juego
    visitados = set()

    print(f"--- Iniciando Dijkstra desde el nodo origen: '{origen}' ---\n")

    # PASO 3: Bucle principal (repetir hasta que no queden nodos por visitar)
    while len(visitados) < len(grafo):
        
        # PASO 1: Elegir el nodo candidato (no visitado) con el menor costo acumulado
        nodo_actual = None
        menor_costo = math.inf

        for nodo in costos:
            if nodo not in visitados and costos[nodo] < menor_costo:
                menor_costo = costos[nodo]
                nodo_actual = nodo

        # Si no quedan nodos alcanzables (o están aislados), cortamos el bucle
        if nodo_actual is None:
            break

        print(f"[*] Marcando como VISITADO el nodo: {nodo_actual} (Costo definitivo: {costos[nodo_actual]})")
        visitados.add(nodo_actual) # ¡Listo, no lo considero nunca más!

        # PASO 2: Relajación de vecinos (Miramos las flechas salientes)
        vecinos = grafo[nodo_actual]
        for vecino, peso_flecha in vecinos.items():
            
            if vecino not in visitados: # Solo evaluamos si aún es candidato
                
                # ACÁ ESTÁ EL SECRETO: Usamos SIEMPRE el costo actualizado del nodo en el que estamos parados
                costo_hacer_escala = costos[nodo_actual] + peso_flecha
                
                # PASO 2A: Comparamos ofertas
                if costo_hacer_escala < costos[vecino]:
                    print(f"    -> ¡Ganga! Llegar a '{vecino}' haciendo escala en '{nodo_actual}' cuesta {costo_hacer_escala}. (Antes costaba {costos[vecino]})")
                    costos[vecino] = costo_hacer_escala

    # Imprimimos la tabla final resultante
    print("\n--- TABLA FINAL (Costos mínimos) ---")
    for nodo, costo in costos.items():
        print(f"Nodo {nodo}: {costo}")


# ---------------------------------------------------------
# ARMAMOS EL GRAFO DE TU HOJA
# ---------------------------------------------------------
# Las llaves son los nodos de origen.
# Los valores son sus vecinos con el peso de la arista.
grafo_prueba = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'F': 10},
    'B': {'A': 1, 'C': 8},
    'C': {'F': 2},
    'F': {}  # El nodo F no tiene flechas salientes (Paso 2B: No hace nada)
}

# Ejecutamos
dijkstra_simple(grafo_prueba, 'S')
