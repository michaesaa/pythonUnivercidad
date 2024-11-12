notas = []
for i in range(5):
    nota = float(input("Ingrese la nota {i + 1} (entre 1 y 5): "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

if promedio >= 3:
    print("El estudiante aprueba la materia.")
else:
    print("El estudiante no aprueba la materia.")
