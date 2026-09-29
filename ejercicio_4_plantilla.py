def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero


def restar(primer_numero, segundo_numero):
    return primer_numero - segundo_numero


def multiplicar(primer_numero, segundo_numero):
    return primer_numero * segundo_numero


def dividir(primer_numero, segundo_numero):
    if segundo_numero == 0:
        raise ZeroDivisionError("No se puede dividir entre 0.")
    return primer_numero / segundo_numero


def es_par(numero):
    return numero % 2 == 0


def calculadora():
        print("\n--- CALCULADORA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Verificar si un número es par")
        print("6. Salir")
        
while True:

            opcion = input("Elige una opción: ")
        # Completa aquí usando match/case.
            match opcion:

                case 1: 
                    print("Estas en una suma")
                case 2:
                    print("Estas en una resta")
                case 3:
                    print("Estas en una multiplicación")
                case 4:
                    print("Estas en una división")
                case 5:
                    print("Estas verificando si este número es par")
                case 6:
                    print("Hasta luego")
