import random

print("*********************************************+")
print("Bienvenido al juego de adivinanza de números!")
print("*********************************************+")

min_num = 1
max_num = 100
numero_a_adivinar = random.randint(min_num, max_num)
num_intentos = 10

print(f"Adivina un número entre {min_num} y {max_num}. Tienes {num_intentos} intentos.")

for intento_actual in range(1, num_intentos + 1):
    # Pedir al usuario que ingrese un número válido
    while True:
        numero_ingresado_str = input(f"Intento {intento_actual}. Ingresa un número: ")
        if not numero_ingresado_str.isdigit():
            print("Por favor ingresa un número entero válido.")
        else:
            numero_ingresado = int(numero_ingresado_str)
            break

    if numero_ingresado == numero_a_adivinar:
        print("¡Felicidades! Adivinaste el número.")
        break

    if numero_ingresado < numero_a_adivinar:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")

    if intento_actual == num_intentos:
        print(f"Lo siento, has agotado tus {num_intentos} intentos. El número correcto era {numero_a_adivinar}.")
