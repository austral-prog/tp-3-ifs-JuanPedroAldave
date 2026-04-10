from tkinter.filedialog import dialogstates


def weekday():

    Dia = input().lower()
    if not (Dia == "sabado" or Dia == "domingo"):
        print("Dia habil")
    else:
        print("Fin de semana")


