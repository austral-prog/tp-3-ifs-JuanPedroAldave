def password():

    contraseña = input()
    longitud = len(contraseña)
    numero = str(0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9)
    if longitud >= 8 and (numero in contraseña):
        print("Contraseña valida")
    elif longitud < 8 and (numero in contraseña):
        print("Contraseña muy corta")
    elif longitud >= 8 and (numero not in contraseña):
        print("Debe contener un numero")
    else:
        print("""Contraseña muy corta
Debe contener un numero""")




