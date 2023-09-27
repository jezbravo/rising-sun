import random

pistas_posibles = {
    "uno":    "_|_|_",
    "dos":    "__|||||",
    "tres":   "__|___|___|___|___|___|___|___",
    "cuatro": "__||___|___||___|___||___|___||___",
    "cinco":  "__|_|__|___|__|_|______",
    "seis":   "__||_|___||_|___||_|___||___"
}

print("""
    Genere una función que evalúe si el jugador recorre la pista sin errores.
    Por cada '_' de la pista random debe haber una 'C' y por cada '|' de valla una 'S'.
    Si el usuario ingresó uno o más espacios " ", reemplázalos por "".
    Si hay caracteres que no son '_' o '|', será un error.
    Si hay más 'C' + 'S' que '_' + '|', será un error.

    Si no hay errores, el resultado será "exito".
    Si hay errores, el resultado será "errores".

Ejemplo 1:
    pista   = _ _ _ | _ _ _ | | _ _ _
              C C C S C C C S S C C C
             
    solucion = CCCSCCCSSCCC

    El jugador recorrió la pista con éxito.
---------------------------------------------------

Ejemplo 2:
    pista   = _ _ _ | _ _ _ | | _ _ _
              C C S S C C C S C C C C
                  ^__errores__^
             
    solucion = CCSSCCCSCCCC

    El jugador recorrió la pista con errores.

---------------------------------------------------
""")
input("Enter para continuar")

def chequear_pista(pista_jugador, pista_random):
    pista_jugador = pista_jugador.replace(" ", "")
    print(f"Número de pista: {pista_random}")
    print(pista_jugador)

    contador_c = pista_jugador.count("C")
    contador_s = pista_jugador.count("S")
    contador_guiones = pista_random.count("_")
    contador_vallas = pista_random.count("|")

    if contador_c + contador_s != contador_guiones + contador_vallas:
        return "errores"
    else:
        return "éxito!"

ganadas = 0
perdidas = 0

for contador in range(1, 11):
    pista_random = random.choice(list(pistas_posibles.keys()))
    print(f"La pista elegida es la número {pista_random}")
    print(pistas_posibles[pista_random])
    pista_jugador = input("Ingrese S) para saltar por cada | y C) para correr por cada _\n>").upper()

    resultado = chequear_pista(pista_jugador, pistas_posibles[pista_random])
    print(f"El jugador recorrió la pista con {resultado}")

    if resultado == "éxito!":
        ganadas += 1
    elif resultado == "errores":
        perdidas += 1

    print("*" * 50)

print(f"Partidas ganadas: {ganadas}")
print(f"Partidas perdidas: {perdidas}")