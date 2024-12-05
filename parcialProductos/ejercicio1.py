def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vocales)

texto = input("Ingrese un texto: ")
print(f"El texto tiene {contar_vocales(texto)} vocales.")
