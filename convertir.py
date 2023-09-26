import math

control = True

sino = ["si", "no"]
while True == True:
    pregunta = input("Deseas convertir angulos a radianes? Responde con un si o no: ").lower()
    try:
        si_o_no = str(pregunta)
        if isinstance(si_o_no, str) == True and pregunta in sino:
            control == False
            if pregunta == "si":
                angulo_radian = input("Ingresa el valor del angulo en grados para convertir a radianes: ")

                angulo_radian = int(angulo_radian)
                conversion = math.pi / 4
                radianes1 = math.radians(conversion)

                print(angulo_radian, "grados en radianes son: ", conversion)
                break
            elif pregunta == "no":
                radian_angulo = input("Ingresa el valor en radianes para convertirlo en grados: ")

                radian_angulo = float(radian_angulo)
                division = math.pi / 4
                grados = math.degrees(radian_angulo)

                print(radian_angulo, "radianes en grados son: ", grados)
                break
        else:
            print("Utiliza caracteres validos..")
            continue
    except Exception:
        print("Utiliza caracteres validos.")
        continue

continuar = input("Deseas terminar el programa?: ")
if continuar == "si":
    print("Okay! hasta la proxima")