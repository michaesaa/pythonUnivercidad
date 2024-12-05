numeros = []
while len(numeros) < 5:
    numero = int(input(f"Ingrese un número positivo ({len(numeros) + 1}/5): "))
    if numero >= 0:
        numeros.append(numero)

print("Sumatoria de los números:", sum(numeros))
