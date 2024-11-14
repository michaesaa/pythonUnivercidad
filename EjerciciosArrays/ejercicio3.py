listaPalabras = []

preguntar = int(input("cuantas palabras desea ingresar: "))

for i in range(preguntar):
    palabra = input(f"ingrese una palabra: {i+1}: ")
    listaPalabras.append(palabra)

pregunta = str(input("ingrese una palabra a sustituir: "))
pregunta2 = str(input("ingrese una palabra para sustituir: "))

for i in range(len(listaPalabras)):
    if pregunta == listaPalabras[i]:
        listaPalabras[i] = pregunta2
    print(listaPalabras[i])