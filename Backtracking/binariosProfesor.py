def binNum(num):
    resultado = []

    def binNumRecursivo(solParcial, num):
        #Caso Base
        if len(solParcial) == num:
            print(solParcial)
            resultado.append("".join(str(bit) for bit in solParcial)) #convertimos la lista de bits a string para guardarla
            return
        
        else:
            #debo seguir completando el numero binario
            for i in range(2):
                solParcial.append(i)
                binNumRecursivo(solParcial,num) #pasamos siempre num porque el numero de digitos no cambia
                solParcial.pop() #sacamos el ultimo elemento para probar con el siguiente

    binNumRecursivo([],num)
    return resultado

if __name__ == "__main__":
    n = 3
    a = binNum(n)

    print("Lista:", a)
