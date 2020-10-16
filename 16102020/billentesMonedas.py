print("\tBilletes y Monedas")


while True:
    try:
        N = float(input("Cuánto dinero tienes: "))
        break
    except:
        print("¡Cantidad inválida!")

print("NOTAS:")
billetes100 = 0
while True:
    if N - 100 >= 0:
        billetes100 += 1
        N -= 100
    else:
        break
print("{} nota(s) de R$ 100.00".format(billetes100))

billetes50 = 0
while True:
    if N - 50 >= 0:
        billetes50 += 1
        N -= 50
    else:
        break
print("{} nota(s) de R$ 50.00".format(billetes50))

billetes20 = 0
while True:
    if N - 20 >= 0:
        billetes20 += 1
        N -= 20
    else:
        break
print("{} nota(s) de R$ 20.00".format(billetes20))


billetes10 = 0
while True:
    if N - 10 >= 0:
        billetes50 += 1
        N -= 10
    else:
        break
print("{} nota(s) de R$ 10.00".format(billetes10))

billetes5 = 0
while True:
    if N - 5 >= 0:
        billetes5 += 1
        N -= 5
    else:
        break
print("{} nota(s) de R$ 5.00".format(billetes5))

billetes2 = 0
while True:
    if N - 2 >= 0:
        billetes2 += 1
        N -= 2
    else:
        break
print("{} nota(s) de R$ 2.00".format(billetes2))


print("\nMONEDAS\n")

monedas1 = 0
while True:
    if N - 1 >= 0:
        monedas1 += 1
        N -= 1
    else:
        break
print("{} moneda(s) de R$ 1.00".format(monedas1))

monedas050 = 0
while True:
    if N - .50 >= 0:
        monedas050 += 1
        N -= .50
    else:
        break
print("{} moneda(s) de R$ 0.50".format(monedas050))

monedas025 = 0
while True:
    if N - .25 >= 0:
        monedas025 += 1
        N -= .25
    else:
        break
print("{} moneda(s) de R$ 0.25".format(monedas025))

monedas010 = 0
while True:
    if N - .10 >= 0:
        monedas010 += 1
        N -= .10
    else:
        break
print("{} moneda(s) de R$ 0.10".format(monedas010))

monedas0050 = 0
while True:
    if N - .050 >= 0:
        monedas0050 += 1
        N -= .050
    else:
        break
print("{} moneda(s) de R$ 0.05".format(monedas0050))

monedas0010 = 0
while True:
    if N - 0.010 >= 0:
        monedas0010 += 1
        N -= .010
    else:
        break
print("{} moneda(s) de R$ .01".format(monedas0010))
