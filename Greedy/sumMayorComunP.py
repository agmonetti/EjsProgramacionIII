def maxima_suma_comun(p1, p2, p3):
    # Damos vuelta las listas para que el "tope" (el primer número según el parcial)
    # quede al final de la lista de Python. Así pop() es ultra eficiente O(1).
    # P1 pasa de [5, 4, 1, 1, 1] a [1, 1, 1, 4, 5]
    pila1 = p1[::-1]
    pila2 = p2[::-1]
    pila3 = p3[::-1]

    # Calculamos la sumatoria inicial de cada pila
    sum1 = sum(pila1)
    sum2 = sum(pila2)
    sum3 = sum(pila3)

    # Mientras haya una diferencia entre las sumas...
    while not (sum1 == sum2 == sum3):
        
        # Si alguna pila se queda vacía y no logramos igualarlas, 
        # el único punto de encuentro posible es 0.
        if not pila1 or not pila2 or not pila3:
            return 0
        
        # Estrategia Greedy: Atacamos a la pila con la sumatoria más grande.
        # pop() saca el número del tope y lo restamos de su sumatoria.
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= pila1.pop()
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= pila2.pop()
        else:
            sum3 -= pila3.pop()

    # Si salimos del while, es porque sum1 == sum2 == sum3
    return sum1


# --- PRUEBA CON LOS DATOS DEL PARCIAL ---
# El primer elemento es el "tope" de la pila
P1 = [5, 4, 1, 1, 1]
P2 = [3, 2, 3]
P3 = [1, 2]

resultado = maxima_suma_comun(P1, P2, P3)

print("--- RESULTADO FINAL ---")
print(f"La sumatoria mayor común es: {resultado}")
