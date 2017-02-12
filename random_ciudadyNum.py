import random

def frog():
    ciudades = [ "Las Vegas",
             "Monterrey",
             "Caracas",
             "Colima",
             "Madrid",
             "Estocolmo",
             "Rio",
             "Acapulco",
             "Miami",
             "NY",
            ]
    
    ciudad = random.choice(ciudades)
    listaNum = []
    for i in range(4):
        num = str(random.randint(0,9))
        listaNum.append(num)
    listaNum.sort()
    listaNum.reverse()
    numero = ''.join(listaNum)
    return ciudad + " " + numero

def romanfrog():

    ciudades = [ "Las Vegas",
             "Monterrey",
             "Caracas",
             "Colima",
             "Madrid",
             "Estocolmo",
             "Rio",
             "Acapulco",
             "Miami",
             "NY",
            ]
    
    ciudad = random.choice(ciudades)

    listaNum = []

    for i in range(4):
        num = str(random.randint(0,9))
        listaNum.append(num)

    listaNum.sort()
    listaNum.reverse()

    numero = ''.join(listaNum)

    cifra1 = int(numero[-1])
    cifra2 = int(numero[-2])
    cifra3 = int(numero[-3])
    cifra4 = int(numero[-4])

    if cifra1 <= 3:
        cifra1 = "I" * cifra1
    elif cifra1 == 4:
        cifra1 = "IV"
    elif cifra1 == 5:
        cifra1 = "V"
    elif cifra1 <= 8:
        cifra1 = "V" + "I" * (cifra1 - 5)
    else:
        cifra1 = "IX"

    if cifra2 <= 3:
        cifra2 = "X" * cifra2
    elif cifra2 == 4:
        cifra2 = "XL"
    elif cifra2 == 5:
        cifra2 = "L"
    elif cifra2 <= 8:
        cifra2 = "L" + "X" * (cifra2 - 5)
    else:
        cifra2 = "XC"

    if cifra3 <= 3:
        cifra3 = "C" * cifra3
    elif cifra3 == 4:
        cifra3 = "CD"
    elif cifra3 == 5:
        cifra3 = "D"
    elif cifra3 <= 8:
        cifra3 = "D" + "C" * (cifra3 - 5)
    else:
        cifra3 = "CM"

    cifra4 = "M" * cifra4

    numeroRomano = cifra4 + cifra3 + cifra2 + cifra1

    return ciudad + " " + numeroRomano






























