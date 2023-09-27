from math import pi

def radianes_angulos(radianes):
    grados = (radianes * 180) / pi
    return grados

def angulos_radianes(grados):
    radianes = (grados * pi) / 180
    return radianes

control = True

sino = [1, 2]
while control == True:
    try:
        pregunta = int(input("Escribe 1 si quieres transformar grados a radianes\nEscribe 2 si quieres transformar radianes a grados.\nIntroduzca un numero segun lo que quiers hacer: "))
        valor = float(input("Introduzca el valor que quiere transformar: "))
    except:
        print("Entrada no válida. Por favor, introduzca un número válido.")
        continue

    if pregunta not in sino:
        print("Introduzca una opción válida (1 o 2)")
        control == False
    else:
        if pregunta == 1:
            resultado = angulos_radianes(valor)
            print(valor, "grados son equivalentes a", resultado, "radianes")
        else:
            resultado = radianes_angulos(valor)
            print(valor, "radianes son equivalentes a", resultado, "grados")