import random
import time
import os
def memoria():
    l = []
    print("SE GENERARA UNA SECUENCIA DE 7 NUMEROS MEMORIZALA EN 5 SEGUNDOS")
    for i in range(7):
        x = random.randint(0,9)
        l.append(x)
    print(l)
    time.sleep(5)
    os.system("clear")
    jug = []
    for i in range(7):
        a = int(input())
        jug.append(a)
    if jug == l:
        print("ganaste")
    else:
        print("perdiste")
        print("ERA",l)
    
memoria()

