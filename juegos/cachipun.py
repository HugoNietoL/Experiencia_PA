import random
def cachipun():
    print("Bienvenido al juego del Cachipun")
    j = int(input("Ingresa 1 para piedra\nIngresa 2 para tijera\nIngresa 3 para papel\n"))
    c = random.randint(1,3)
    if j == c:
        print("EMPATEEE")
    elif (j == 1 and c == 2) or (j == 2 and c == 3) or (j == 3 and c == 1):
        print("GANASTEEE")
    elif not( j <=3 and j>= 1):
        print("Ingresa un numero valido")
    else:
        print("PERDISTEEE")
cachipun()