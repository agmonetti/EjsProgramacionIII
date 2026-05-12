"""
- Ordenamos por ganancia.
- vemos en la agenda el horario más tarde posible antes de que venza la tarea.
- Si hay un hueco libre, lo anotamos. Si no, la descartamos.
"""

def planificar_optimizado(ganancias, tiempos):
    cantidad = len(ganancias)
    
    # Juntamos los datos y los ordenamos por ganancia (de mayor a menor)
    # Guardamos (ganancia, plazo, indice_original)
    tareas = [(ganancias[i], tiempos[i], i) for i in range(cantidad)]
    tareas.sort(reverse=True, key=lambda x: x[0])

    # Creamos nuestra "agenda" (slots de tiempo).
    tiempo_maximo = max(tiempos) if tiempos else 0
    agenda = [-1] * tiempo_maximo  # -1 significa que el horario está libre

    for ganancia, plazo, indice_tarea in tareas:
        # Buscamos de atrás para adelante (desde su plazo límite hacia la hora 0)
        for hora in range(min(tiempo_maximo, plazo) - 1, -1, -1):
            if agenda[hora] == -1: # Si el hueco está libre
                agenda[hora] = indice_tarea # Metemos la tarea ahí
                break # Pasamos a la siguiente tarea

    # Limpiamos los huecos que hayan quedado vacíos
    resultado = [tarea for tarea in agenda if tarea != -1]
    return resultado

# --- EJEMPLO DEL APUNTE ---
# (g1, g2, g3, g4)
ganancias = [50, 10, 15, 30]

# (t1, t2, t3, t4)
tiempos = [2, 1, 2, 1]

secuencia_correcta = planificar_optimizado(ganancias, tiempos)

# Le sumamos 1 a los índices para que se lea como "Tarea 1, Tarea 2, etc."
secuencia_humana = [t + 1 for t in secuencia_correcta]

print(f"Ganancias: {ganancias}")
print(f"Tiempos límite: {tiempos}")
print(f"Secuencia óptima encontrada: {secuencia_humana}")