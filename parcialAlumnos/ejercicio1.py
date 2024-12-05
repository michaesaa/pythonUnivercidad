def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

numero = int(input("ingrese el nuemro para tabla de miltiplicar: "))

tabla_multiplicar(numero)