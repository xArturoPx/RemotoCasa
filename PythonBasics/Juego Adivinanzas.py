import random

def juego():
    # Inicialización de variables
    intentos_restantes = 10
    rango_min = 1
    rango_max = 10
    numero_a_adivinar = random.randint(rango_min, rango_max)

    # Ciclo principal del juego
    while intentos_restantes > 0:
        # Muestra la cantidad de intentos restantes
        print(f"Te quedan {intentos_restantes} intentos")
        # Pide al usuario que adivine el número
        numero_elegido = input(f"Adivina un número entre {rango_min} y {rango_max}: ")

        # Validación de la entrada del usuario
        while not numero_elegido.isdigit():
            print("Por favor, ingresa un número.")
            numero_elegido = input(f"Adivina un número entre {rango_min} y {rango_max}: ")
        numero_elegido = int(numero_elegido)

        # Validación de que el número esté dentro del rango
        if numero_elegido < rango_min or numero_elegido > rango_max:
            print(f"Por favor, ingresa un número entre {rango_min} y {rango_max}.")
            continue

        # Compara el número elegido con el número a adivinar
        if numero_elegido == numero_a_adivinar:
            # Mensaje de éxito en la adivinanza
            print("--------------------------------------------")
            print(f"¡Felicidades, adivinaste el número!: -> {numero_a_adivinar} <-")
            print(f"Te sobraron {intentos_restantes} intentos")
            print("Te añadiremos 10 intentos !Buena Suerte¡")
            print("¡Vamos por otro!")
            print("¡Subiremos la dificultad!")
            print("--------------------------------------------")

            # Aumenta la dificultad del juego y reinicia los intentos y el número a adivinar
            rango_max += 10
            intentos_restantes += 10
            numero_a_adivinar = random.randint(rango_min, rango_max)

        elif numero_elegido < numero_a_adivinar:
            # Mensaje de que el número es más grande
            print("El número es más mayor")
            intentos_restantes -= 1
        else:
            # Mensaje de que el número es más chico
            print("El número es más ")
            intentos_restantes -= 1

    # Mensaje de fin del juego
    print("¡Se te acabaron los intentos! Perdiste :(")
