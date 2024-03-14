import random
def juego_del_dado():
    upuntos = 0
    cpuntos = 0
    while True:
        enter = input("apreta enter")
        if enter == "":
            numero1 = random.randint(1,6)
            upuntos = upuntos + numero1
            numero2 = random.randint(1,6)
            cpuntos = cpuntos + numero2
            print(upuntos)
            print(cpuntos)
            if upuntos >= 30:
                print("gana usuario")
                break
            elif cpuntos >= 30:
                print("gana compu")
                break
            
juego_del_dado()




"""
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.


    """