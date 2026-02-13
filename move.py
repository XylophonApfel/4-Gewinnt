import generate_board

def move():
    while True:
        try:
            move_Zeile = int(input("Bitte gebe die Zeile ein (1-6):\n "))
            if 1 <= move_Zeile <= 6:
                break
            else:
                print("Zahl muss zwischen 1 und 6 liegen.")
                continue
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

        move_Spalte= int(input("Bitte die Spalte eingeben (1-7): \n"))
    while True:
        try:
            move_Spalte= int(input("Bitte die Spalte eingeben (1-7): \n"))
            if 1 <= move_Spalte <= 6:
                break
            else:
                print("Zahl muss zwischen 1 und 6 liegen.")
                continue
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

move()
