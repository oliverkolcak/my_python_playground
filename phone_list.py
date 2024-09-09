phone_list = ['702554789','788945321','111222333']
y = True
while y:
    try:
        x = int(input("Ahoj. Toto je seznam telefonnich cisel. Chces:\n1. Pridat telefonni cislo.\n2. Odstranit telefonni cislo.\n3. Vypsat seznam telefonnich cisel.\n4. Ukoncit aplikaci.\n\nZvol jednu z moznosti: "))
    except ValueError:
        x = 5
    match x:
        case 1:
            z = input("Pridat cislo do seznamu: ")
            try:
                w = int(z)
                if len(z) >= 9 and len(z) <= 14:
                    phone_list.append(z)
                    print("Telefonni cislo pridano.\n")
                else:
                    print("Nejedna se o telefonni cislo. Prosim zkuste to znovu.\n")
            except ValueError:
                print("Nejedna se o telefonni cislo. Prosim zkuste to znovu.\n")
        case 2:
            z = input("Odstranit telefonni cislo z seznamu: ")
            for number in phone_list:
                if z == number:
                    phone_list.remove(z)
                    print("Telefonni cislo odstraneno.\n")
                    break
                else:
                    print("Telefonni cislo nenalezeno. Prosim zkuste to znovu.\n")
        case 3:
            i = 1
            print("Seznam telefonnich cisel: ")
            for number in phone_list:
                print(f"{i}. "+ number)
                i += 1
            print()
        case 4:
            y = False
        case _:
            print("Nespravne zadana moznost.\n")