def simular_planificacion(tareas, nombre_estrategia):
    tiempo_actual = 0
    max_demora = 0
    
    print(f"\n=== Estrategia: {nombre_estrategia} ===")
    print(f"{'Tarea':<6} | {'Inicio (s)':<10} | {'Fin (f)':<8} | {'Plazo (d)':<10} | {'Demora (l)'}")
    print("-" * 55)
    
    for nombre, t, d in tareas:
        inicio = tiempo_actual
        fin = inicio + t
        demora = max(0, fin - d)
        
        # Actualizamos la máxima demora si la actual es peor
        if demora > max_demora:
            max_demora = demora
            
        tiempo_actual = fin # El tiempo avanza
        
        print(f"{nombre:<6} | {inicio:<10} | {fin:<8} | {d:<10} | {demora}")
        
    print("-" * 55)
    print(f">>> DEMORA MÁXIMA GLOBAL (L): {max_demora}\n")


# --- DATOS DEL PROBLEMA ---
# Formato: (Nombre_Tarea, tiempo_procesamiento_tj, plazo_dj)
tareas_originales = [
    ("X1", 26, 24),
    ("X2", 30, 25),
    ("X3", 15, 14),
    ("X4", 10, 80) # Una tarea con plazo recontra holgado para estorbar
]

# 1. Simulación SIN Greedy (Ejecutar en el orden caótico en el que llegaron)
simular_planificacion(tareas_originales, "Orden Original (Caótico)")

# 2. Simulación CON Greedy (Regla de Jackson: Ordenar por menor plazo d_j)
# Usamos sorted() de Python diciéndole que ordene por el índice 2 de la tupla (el plazo)
tareas_greedy = sorted(tareas_originales, key=lambda x: x[2])
simular_planificacion(tareas_greedy, "Algoritmo Greedy (Menor Plazo Primero)")
