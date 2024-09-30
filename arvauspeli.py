import random

def arvauspeli():
    numero = random.randint(1, 1000)
    yritykset = 0
    print("Arvaa numero 1 ja 1000 välillä!")

    while True:
        arvaus = input("Anna arvauksesi: ")
        
        if not arvaus.isdigit():
            print("Anna vain numeroita!")
            continue
        
        arvaus = int(arvaus)
        yritykset += 1

        if arvaus < numero:
            print("Liian pieni!")
        elif arvaus > numero:
            print("Liian suuri!")
        else:
            print(f"Onneksi olkoon! Arvasit oikein numeron {numero} {yritykset} yrityksellä!")
            break

if __name__ == "__main__":
    arvauspeli()
