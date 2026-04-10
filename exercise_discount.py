def discount():

    precio = float(input())
    cantidad = int(input())
    subtotal = precio * cantidad
    if cantidad >= 10:
        descuento = subtotal * 0.2
    elif(cantidad >= 5 and cantidad <= 9):
        descuento = subtotal * 0.1
    else:
        descuento = subtotal * 0
    print(f"Subtotal: {subtotal}")
    if cantidad >= 10:
        print("Descuento aplicado: 20%")
    elif(cantidad >= 5 and cantidad <= 9):
        print("Descuento aplicado: 10%")
    else:
        print("Descuento aplicado: 0%")
    print(f"Monto de descuento: {descuento}")
    print(f"Total final: {subtotal - descuento}")




