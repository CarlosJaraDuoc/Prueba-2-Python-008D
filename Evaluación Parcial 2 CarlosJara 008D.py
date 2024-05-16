import os
import time
clean = "cls"
camion = 765000
multa = 100000
os.system(clean)
while True:
        print("Bienvenido cliente")
        print("Ingrese su nombre (debe poseer mínimo 3 letras): ")
        nombre = str(input())
        if len(nombre) < 3:
            print("Debe ingresar mínimo 3 letras. ")
            time.sleep(1)
            continue
    camion %= multa
    print(camion)
    while True:
        try:
            otro = int(input("¿Desea hacer otro pedido?:\n1. Otro pedido \n2. Salir del programa\n" ))
            if otro == 1:
                break
            elif otro == 2:
                break
            else:
                print("Solo puede ingresar los valores 1 y 2.")
        except ValueError:
            print("Ingrese un valor válido (1 o 2)")
            time.sleep(2)
            continue
    if otro == 1:
        os.system(clean)
        time.sleep(1)
        continue
    else:
        print("Gracias por usar el programa.")
        time.sleep(1)
        break


