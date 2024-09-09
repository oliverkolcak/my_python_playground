import random
x = random.randint(1,100)
y = True
while y == True:
    z = int(input("Hadej cislo: "))
    if z == x:
        print("JE TO TAM!!!!!")
        break
    elif x > z:
        print("Nene. Jedna se o vetsi cislo.")
    elif x < z:
        print("Nene. Jedna se o mensi cislo")
    """
    match z:
        case z if x > z:
            print("Nene. Jedna se o vetsi cislo.")
        case z if x < z:
            print("Nene. Jedna se o mensi cislo.")
    """