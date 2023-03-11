def leer_conjunto(mensaje):
    numeros = input(mensaje).split(",")
    conjunto = set()

    for num in numeros:
        try:
            num = int(num)
            if num in conjunto:
                print("Error: los números deben ser únicos.")
                return leer_conjunto(mensaje)
            conjunto.add(num)
        except ValueError:
            print("Error: debe ingresar números enteros separados por comas.")
            return leer_conjunto(mensaje)

    return conjunto

def union(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def interseccion(conjunto1, conjunto2):
    interseccion = conjunto1.intersection(conjunto2)
    if not interseccion:
            print("No se nota interseccion alguna")
    return interseccion
def diferencia(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

def diferencia_simetrica(conjunto1, conjunto2):
    return conjunto1.symmetric_difference(conjunto2)

def main():
    while True:
        print("---------------------------")
        print("Calculadora de Conjuntos")
        print("----------------------------")
        print("0 - Salir")
        print("1 - Unión")
        print("2 - Intersección")
        print("3 - Diferencia")
        print("4 - Diferencia Simétrica")

        opcion = input("\nIngrese una opción: ")

        # Utilizamos la estructura match para las opciones
        match opcion:
            case "0":
                print("¡Hasta luego!")
                return

            case "1":
                conjunto1 = leer_conjunto("Ingrese los números del primer conjunto separados por comas: ")
                conjunto2 = leer_conjunto("Ingrese los números del segundo conjunto separados por comas: ")
                resultado = union(conjunto1, conjunto2)
                print("-------------------------------------------------------------")
                print("La unión de los conjuntos es:", resultado)
                print("-------------------------------------------------------------")

            case "2":
                conjunto1 = leer_conjunto("Ingrese los números del primer conjunto separados por comas: ")
                conjunto2 = leer_conjunto("Ingrese los números del segundo conjunto separados por comas: ")
                resultado = interseccion(conjunto1, conjunto2)
                if resultado:
                    print("-------------------------------------------------------------")
                    print("La intersección de los conjuntos es:", resultado)
                    print("-------------------------------------------------------------")
                else:
                    print("-------------------------------------------------------------")
                    print("Los conjuntos no tienen intersección.")
                    print("-------------------------------------------------------------")
            case "3":
                conjunto1 = leer_conjunto("Ingrese los números del primer conjunto separados por comas: ")
                conjunto2 = leer_conjunto("Ingrese los números del segundo conjunto separados por comas: ")
                resultado = diferencia(conjunto1, conjunto2)
                print("-------------------------------------------------------------")
                print("La diferencia del primer conjunto con respecto al segundo es:", resultado)
                print("-------------------------------------------------------------")

            case "4":
                conjunto1 = leer_conjunto("Ingrese los números del primer conjunto separados por comas: ")
                conjunto2 = leer_conjunto("Ingrese los números del segundo conjunto separados por comas: ")
                resultado = diferencia_simetrica(conjunto1, conjunto2)
                print("-------------------------------------------------------------")
                print("La diferencia simétrica de los conjuntos es:", resultado)
                print("-------------------------------------------------------------")

            case _:
                print("Opción inválida. Intente nuevamente.")

main()