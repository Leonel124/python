import random

# Se le pregunta el nombre al jugador
nombre = input("Bienvenido al juego por favor introduzca su nombre de usuario: ")
# Se imprime el nombre del jugador junto a las reglas del juego
print("Hola,", nombre, " para poder jugar necesita conocer las reglas de este juego las cuales son: \n1.-La computadora eligira una palabra al azar.\n2.-Cuentas con SOLO 6 VIDAS.\n3.-La computadora mostrara los espacios de la palabra oculta cada vez que haga un intento.\n4.-El jugador que intenta adivinar comenzará a decir sus letras y en caso de acertar una letra, se colocará en el espacio correspondiente.\n5.-En el caso de no acertar, perderas una vida por cada intento fallido.\n6.-Si el jugador no adivina la palabra al final de sus 6 vidas el juego finalizara y tendra que repetir si desea jugar de nuevo.\n")


# Lista de palabras que la computadora escogera
palabras = ["botella", "control", "telefono", "computadora", "raton", "teclado"]

# Elige una palabra al azar de la lista.
palabra = random.choice(palabras)

# Crea una cadena de guiones bajos para ocultar la palabra.
palabra_oculta = "_" * len(palabra)

errores = 0
letras_escritas = []

abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def vidas_restantes(rr):
    if rr == 1:
        return("Quedan 5 vidas")
    elif  rr == 2:
        return("Quedan 4 vidas")
    elif rr == 3:
        return("Quedan 3 vidas")
    elif rr == 4:
        return("Quedan 2 vidas")
    elif rr == 5:
        return("Queda 1 vida")
    elif rr == 6:
        # Muestra la palabra que la compu eligio cuando el jugador pierde
        return ("Perdiste. Inténtalo de nuevo :/")

ayuda = ["a"]
print("La palabra oculta: ", palabra_oculta)

# Bucle principal del juego.
while errores <= 6:

 letra = input("Ingresa una letra: ").lower()
    # Verifica si la palabra que puso ya la habia escrito
 if letra not in abecedario:
     print("Ese caracter no es una letra.")
 else:
    if letra in letras_escritas:
        print("Ya has puesto esa letra. Intenta de nuevo.")
    elif letra in palabra:
        # Actualiza los espacios de la palabra oculta con letras que el jugador dijo.
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta = palabra_oculta[:i] + letra + palabra_oculta[i + 1:]
        print("La palabra es:", palabra_oculta)
        if "_" not in palabra_oculta:
            print("Ganaste")
            break
    else:
        errores += 1
        print(vidas_restantes(errores))
        letras_escritas.append(letra)
        if errores == 6:
            break