estudent_list = []
notaList = []

for i in range(5):
    name = input("Ingrese el nombre del estudiante: ")
    estudent_list.append(name)




for i in range(len(estudent_list) ):
    while True:
        nota = float(input("Ingrese la nota del estudiante: "))
        if nota >= 0 and nota <= 5:
            notaList.append(nota)
            break
        else:
            print("La nota debe estar entre 0 y 5. Intente nuevamente.")

while True:
    nota = float(input("Ingrese la nota del estudiante: "))
    if nota >= 0 and nota <= 5:
        notaList.append(nota)
        break
    else:
        print("La nota debe estar entre 0 y 5. Intente nuevamente.")
