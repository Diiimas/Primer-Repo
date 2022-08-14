a1 = 9
if (a1 < 0):
    print ("el numero es negativo")
elif (a1 > 0):
    print ("el numero es positivo")

    a2 = "dato"
a3 = 6
if (type(a2) == type(a3)):
    print ("Misma clase de dato")
elif (type (a2) != type (a3)):
    print ("Distintos tipos de datos")

for i in range (1, 21):
    if (i % 2 == 0):
        print("El numero", i ,"es par")
    elif (i % 2 != 0):
        print("el numero", i ,"es impar")

for b in range (0,6):
    print("el numero", b , "elevado a la tercer potencia es", b**3)

c = 5
d = 1
for i in range(d, c):
    continue