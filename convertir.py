from math import pi

def radianes_angulos(radianes):
    grados = (radianes * 180) / pi
    return grados

def angulos_radianes(grados):
    radianes = (grados * pi) / 180
    return radianes

control = True
sino = [1, 2]

while control = True:
    try:
        pregunta = int(input(
            "Escribe 1 si quieres transformar grados a radianes\nEscribe 2 si quieres transformar radianes a grados.\nIntroduzca el numero correspondiente segun lo que quieres hacer: "))
        valor = float(input("Introduzca el valor que quieres transformar: "))

        if valor <= 0:
            print("Introduzca un caracter valido. ")
        else:
            if pregunta not in sino:
                print("Introduzca una opción válida. ")
            else:
                if pregunta == 1:
                    resultado = angulos_radianes(valor)
                    print(valor, "grados son equivalentes a", resultado, "radianes")
                    control = False
                else:
                    resultado = radianes_angulos(valor)
                    print(valor, "radianes son equivalentes a", resultado, "grados")
                    control = False
    except ValueError:
        print("Caracter invalido. Por favor, introduzca un caracter valido")