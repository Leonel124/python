def verificacion():
    while True:
        pide_el_angulo = input("Introduzca el valor de un angulo en grados para determinar su tipo: ")

        try:
            angulo = int(pide_el_angulo)
            return angulo
        except Exception:
            print("Introduce un numero valido ")

def grados(angulo):
    if angulo >= 0 and angulo < 90:
        return "Tu angulo es agudo"
    elif angulo == 90:
        return "Tu angulo es recto"
    elif angulo > 90 and angulo < 180:
        return "Tu angulo es obtuso"
    elif angulo == 180:
        return "Tu angulo es llano o colineal"
    elif angulo > 180 and angulo < 360:
        return "Tu angulo es entrante o convexo"
    elif angulo == 360:
        return "Tu angulo es perigono"

angulo = verificacion()
resultado = grados(angulo)
print(resultado)