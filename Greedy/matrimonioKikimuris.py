def algoritmo_kikimuris(pref_hombres, pref_mujeres):
    # Clonamos las listas de los hombres para poder usar .pop(0) 
    # y simular el "tachar de la lista" sin perder los datos originales.
    candidatas = {h: list(mujeres) for h, mujeres in pref_hombres.items()}
    
    # Línea 2: Inicialmente todos están libres
    hombres_libres = list(pref_hombres.keys())
    parejas_mujeres = {} # Diccionario para guardar el estado: {Mujer: Hombre actual}

    # Línea 3: Mientras haya un hombre libre...
    while hombres_libres:
        # Línea 4: Elegir m
        m = hombres_libres[0] 
        
        # Línea 5: Elegir f (la primera de su lista que quede) y la sacamos
        f = candidatas[m].pop(0) 
        
        print(f"\n-> {m} le propone matrimonio a {f}")

        # Línea 6: Si f está libre
        if f not in parejas_mujeres:
            # Línea 7: Se comprometen
            parejas_mujeres[f] = m
            hombres_libres.remove(m)
            print(f"   ¡{f} estaba libre! Se comprometen ({m}, {f}).")
        
        # Línea 8: sino (f está comprometida con m')
        else:
            m_prima = parejas_mujeres[f]
            print(f"   {f} ya está comprometida con {m_prima}.")
            
            # Para saber a quién prefiere, vemos quién está primero (menor índice) en su lista
            lista_f = pref_mujeres[f]
            
            # Línea 11: Si f prefiere a m (el nuevo)
            if lista_f.index(m) < lista_f.index(m_prima):
                # Línea 12: Se comprometen
                parejas_mujeres[f] = m
                hombres_libres.remove(m)     # El nuevo deja de estar libre
                # Línea 13: m' queda libre
                hombres_libres.append(m_prima) 
                print(f"   ¡Pero {f} prefiere a {m}! Patea a {m_prima}. El ex vuelve a estar libre.")
            
            # Línea 9: Si f prefiere a m' (su pareja actual)
            else:
                # Línea 10: m continúa libre
                print(f"   {f} prefiere quedarse con {m_prima}. {m} es rechazado y sigue libre.")
                
    # Línea 17: Devolver la lista
    return parejas_mujeres

# --- LOS DATOS DE NUESTRO EJEMPLO ---
preferencias_hombres = {
    "H1": ["M1", "M2", "M3"],
    "H2": ["M1", "M3", "M2"],
    "H3": ["M1", "M2", "M3"]
}

preferencias_mujeres = {
    "M1": ["H2", "H3", "H1"],
    "M2": ["H1", "H2", "H3"],
    "M3": ["H1", "H2", "H3"]
}

# Ejecutamos
resultado = algoritmo_kikimuris(preferencias_hombres, preferencias_mujeres)

print("\n=== RESULTADO FINAL ESTABLE ===")
for mujer, hombre in resultado.items():
    print(f"Pareja: ({hombre}, {mujer})")
