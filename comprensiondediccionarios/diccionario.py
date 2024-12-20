# nuevo_diccionario = {clave: valor for elemento in secuencia }

numeros = [1,2,3,4,5,6,7,8,9,10]
diccionario_cuadrados = {num: num**2 for num in numeros}
print(numeros)
print(diccionario_cuadrados)

print("*"*50)

numeros = [1,2,3,4,5,6,7,8,9,10]
diccionario_par = {num:num for num in numeros if num % 2 == 0}
print(numeros)
print(diccionario_par)


print("*"*80)


print("longitud de palabras de una lista de cadenas") 
palabras = ["python","con",".randon"]
diccionario_longitudes = {palabra: len(palabra) for palabra in palabras}
print(diccionario_longitudes)