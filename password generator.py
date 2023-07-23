import random as rd

def generer_passord():
    små_bokstaver = "abcdefghijklmnopqrstuvwxyzæøå"
    store_bokstaver = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    tegn = "!#$%&/=?+@"
    tall = "0123456789"
    alle_tegn = små_bokstaver + store_bokstaver + tegn + tall
    lengde = 19

    passord = ""
    teller = 0

    for x in range(lengde):
        if teller < 4:
            tilfeldig = rd.randint(0, len(alle_tegn)-1)
            passord += alle_tegn[tilfeldig]
            teller += 1
        else:
            passord += "-"
            teller = 0
        
    print("\nDitt nye passord er: ")
    print(passord + "\n")

generer_passord()
