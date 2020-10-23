    def sumador(*sumandos):
    suma = 0
    
    for n in sumandos:
        suma += n
    return suma
print(f"Con dos argumentos {sumador(3,5)=}")
print(f"Con cuatro argumentos {sumador(4,5,6,7)=}")
print(f"Con cinco argumentos {sumador(1,2,3,5,6)=}")
print(f"Con nueve argumentos {sumador(1,2,3,4,5,6,7,8,9)=}")
print(f"Con cero argumentos {sumador()=}")

