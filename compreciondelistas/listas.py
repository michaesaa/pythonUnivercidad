palabras = ["hola", "mundo", "python"] 
mayusculas = []

for palabra in palabras:
    mayusculas.append(palabra.upper())
print(palabra)
print("*"*30)
print(mayusculas)

# y con comprecion de listas se reduce el codigo

cualquiercosa = ["goku","vegeta","saitama"]

mayusculas = [palabra.upper() for palabra in cualquiercosa]
print("*"*50)
print(mayusculas)


print("*"*80)

# filtrar elementos de una lista

numeros = [1,2,3,4,5,6,7,8,9,10]

mayores_a_cinco = [numero for numero in numeros if numero > 5]
print(numeros)
print(mayores_a_cinco)



# lista de bocales de una cadena 

frase = "phyton es el mejor lenguaje de programacion"
vocales = [letra for letra in frase if letra in "aeiouAEIOU"]
print(frase)
print(vocales)
