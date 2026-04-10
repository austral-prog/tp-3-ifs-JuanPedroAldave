def age_check():

    edad = int(input())
    edadlimite = int(input())
    if edad > 0 and edadlimite > 0:
        if edad >= edadlimite:
            print("Eres mayor de edad")
        elif edad < edadlimite:
            print("Eres menor de edad")
    if edad <= 0 or edadlimite <= 0:
        print("Entrada invalida")
