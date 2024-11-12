pares = 0
impares = 0

for i in range(10):
    num = int(input("Ingrese el número {i + 1}: "))
    if num % 2 == 0:
        print("{num} es par")
        pares += 1
    else:
        print("{num} es impar")
        impares += 1

print("Total de números pares:", pares)
print("Total de números impares:", impares)
