import random
def adivinar_par_o_impar():
    n = random.randint(1,10)
    print("Bienvenido al juego para adivinar si un numero es par o impar")
    pred = input("Ingresa par o impar")
    if n%2 == 0 and pred == "par":
        print("GANASTE!")
    elif n%2 == 1 and pred =="impar":
        print("Ganaste!")
    else:
        print("Perdiste :(")
    
adivinar_par_o_impar()