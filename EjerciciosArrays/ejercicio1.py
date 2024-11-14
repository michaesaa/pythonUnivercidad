palabraList = []

pregunta = int(input("cuantas palabras desea ingresar: "))

for i in range(pregunta):
    palabra = input(f"ingrese una palabra: {i+1}: ")
    palabraList.append(palabra)

pregunta = str(input("ingrese una palabra a buscar: "))
cont = 0

for i in range(len(palabraList)):
    if pregunta == palabraList[i]:
        cont = cont + 1

    if cont > 0:
        print(f"la palabra {pregunta}  se encuentra {cont} veces ")
    else:
        print(f"la palabra {pregunta} no se encuentra en la lista")