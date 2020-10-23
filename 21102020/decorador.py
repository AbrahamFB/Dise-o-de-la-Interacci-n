def decorador(funcion):
    print(80*"-")
    print(80*".")
    funcion()
    print(80*".")
    print(80*"-")
    
@decorador
def ejemplo():
    x = "Hola Mundo"
    print(f"{x:^80}")
