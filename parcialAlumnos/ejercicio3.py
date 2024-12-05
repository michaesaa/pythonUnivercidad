estudiantes = []
notas = []

for i in range(3):  # estudiantes 
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes.append(nombre)
    notas.append(nota)

#estudiantes y notas
for i, estudiante in enumerate(estudiantes):
    print(f"{estudiante}: {notas[i]}")

#Estudiante con la nota más alta
max_nota = max(notas)
max_index = notas.index(max_nota)
print(f"Nota más alta: {estudiantes[max_index]} con {max_nota}")

#Estudiante con la nota más baja
min_nota = min(notas)
min_index = notas.index(min_nota)
print(f"Nota más baja: {estudiantes[min_index]} con {min_nota}")

#Estudiantes que reprobaron y aprobaron
reprobaron = [estudiantes[i] for i in range(len(notas)) if notas[i] < 3.0]
aprobaron = [estudiantes[i] for i in range(len(notas)) if notas[i] >= 3.0]
print("Estudiantes que reprobaron:", reprobaron)
print("Estudiantes que aprobaron:", aprobaron)
