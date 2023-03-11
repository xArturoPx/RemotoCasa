# Función para sumar
def sumar(num1, num2):
    return num1 + num2

# Función para restar
def restar(num1, num2):
    return num1 - num2

# Función para multiplicar
def multiplicar(num1, num2):
    return num1 * num2

# Función para dividir
def dividir(num1, num2):
    return num1 / num2
def validaCero(divisor):
    if( divisor == 0):
        print("      Error: El divisor no puede ser cero (0)")
        return validacion("      Intentelo de nuevo(0 otra vez para salir):")
    else:
        return divisor

def validacion(mensaje, max_intentos=3):
    contador = 0
    while contador < max_intentos:
        try:
            return int(input(mensaje))
        except:
            print("Entero no válido,Intentelo de nuevo")
            contador += 1
    print("Número máximo de intentos alcanzado. Saliendo...")
    exit()
def menu():
    print("")
    print("___________________________________________")
    print("    CALCULADORA DE OPERACIONES BASICAS     ")
    print("___________________________________________")
    print(""
          "OPCIONES")
    print("   0 = Salir")
    print("   1 = Suma")
    print("   2 = Resta")
    print("   3 = Multiplicacion")
    print("   4 = Division")
    return validacion(">Ingrese una opcion:")

while True:
    def main():
        Opcion = menu()
        print("_________________________________")
        print("   Su operacion elegida es: ", Opcion)
        print("_________________________________")

        if Opcion == 0:
            print("Hasta Pronto,Cerrando Calculadora")
        else:
            if Opcion == 1:
                print("EL RESULTADO ES ->",sumar(validacion("     Ingrese su 1er numero:"), validacion("     Ingrese el 2do numero:")),"<-")
            else:
                if Opcion == 2:
                    print("EL RESULTADO ES ->",restar(validacion("     Ingrese su 1er numero:"), validacion("     Ingrese el 2do numero:")),"<-")
                else:
                    if Opcion == 3:
                        print("EL RESULTADO ES ->",multiplicar(validacion("     Ingrese su 1er numero:"), validacion("     Ingrese el 2do numero:")),"<-")
                    else:
                        if Opcion == 4:
                            num1 = validacion("     Ingrese su 1er numero:")
                            num2 = validaCero(validacion("     Ingrese el 2do numero:"))
                            if (num2 != 0):
                                print("EL RESULTADO ES ->",dividir(num1, num2),"<-")
                            else:
                                print("El divisor siegue siendo cero(0) -> Regresando al menu")
                        else:
                            print("Opcion inválida.Regresando al Menu")

    main()
