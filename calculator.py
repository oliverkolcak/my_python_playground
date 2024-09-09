a = float(input("Prvni cislo: "))
x = input("+-*/: ")
b = float(input("Druhe cislo: "))
z = 0
count = True
while count == True:
    match x:
        case "+":
            z = a + b
            print(z)
        case "-":
            z = a - b
            print(z)
        case "*":
            z = a * b
            print(z)
        case "/":
            z = a / b
            print(z)
        case _:
            print("chybny input")
            break
    y = input("Chces pokracovat? ").upper()
    if y == "ANO":
        x = input("+-*/: ")
        b = int(input("Dalsi cislo: "))
    elif y == "NE":
        break
    else:
        print("chybny input")
        break
print()
print(f"Vysledek je {z}")