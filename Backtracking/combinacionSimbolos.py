def obtener_combinaciones(simbolos):
    sol = [None] * len(simbolos)
    soluciones = []
    ejRec(simbolos, sol, 0, soluciones)
    return soluciones

def ejRec(simbolos, sol, i, soluciones):
    if i == len(sol):
        soluciones.append(sol.copy())
        # Opcional: imprimir la solución cuando la encuentra
        print(f"--> ¡SOLUCIÓN ENCONTRADA!: {sol}")
    else:
        for j in range(len(simbolos)):
            sol[i] = simbolos[j]
            
            # EL JUEZ
            if solOk(sol, i):
                ejRec(simbolos, sol, i + 1, soluciones)
            else:
                # ¡ACÁ CAE LA GUILLOTINA! (El paso de la Poda)
                # Imprimimos la porción del arreglo que se intentó armar (hasta el índice i)
                rama_podada = sol[:i+1] 
                print(f"PODA: Descartando {rama_podada} (El símbolo '{simbolos[j]}' ya está usado)")

def solOk(sol, i):
    for k in range(i):
        if sol[k] == sol[i]:
            return False 
    return True 

# --- PRUEBA ---
if __name__ == "__main__":
    simbolos_parcial = ['a', 'b', 'c']
    print(f"Iniciando Backtracking para: {simbolos_parcial}\n")
    obtener_combinaciones(simbolos_parcial)
    
