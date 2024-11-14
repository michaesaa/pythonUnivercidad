num = []
for i in range(10):
    num.append(int(input("Ingrese un número: ")))
print(num)

# oden burbuja
for i in range(len(num) - 1):
    for j in range(len(num) - i - 1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
print("numeros ordenados de mayor a menor",num)  