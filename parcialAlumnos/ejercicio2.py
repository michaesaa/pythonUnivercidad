numeros = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

#Mostrar números pares
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)

#Mostrar números impares
impares = [num for num in numeros if num % 2 != 0]
print("Números impares:", impares)

#Mostrar números negativos
negativos = [num for num in numeros if num < 0]
print("Números negativos:", negativos)
