x = input("Gime me number to check if its palindrom: ")
y = len(x)
z = y - 1
i = 0
for i in range(y):
    if x[i] == x[z]:
        i += 1
        z -= 1
    else:
        print("Not palindrom!")
        break
if z == -1:
    print("PALINDROM!!!")

    