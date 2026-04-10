def triangle():

    lado1 = float(input())
    lado2 = float(input())
    lado3 = float(input())
    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
        print("Los lados forman un triangulo valido")
    else:
        print("Los lados no forman un triangulo valido")


