def adivinar_numero():
    import random
    numero = random.randint(1,10)
    usuario = input("ingrese numero:")
    if numero == usuario:
        print("felicidades, achuntaste el número")
    else:
        print("lastima, no le achuntaste")

adivinar_numero()


"""
Esta función representa el juego de adivinar un número.
Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
Se debe mostrar un mensaje si el usuario adivina correctamente o no.
"""
pass