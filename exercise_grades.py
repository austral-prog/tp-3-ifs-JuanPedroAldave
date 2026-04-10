def grades():

    nota = int(input())
    if nota <= 10 and nota >= 0:
        if nota >= 9:
            print("Excelente")
        elif nota >= 7 and nota <= 8:
            print("Bueno")
        elif nota>=5 and nota <= 6:
            print("Regular")
        elif nota >= 0 and nota <= 4:
            print("Insuficiente")



