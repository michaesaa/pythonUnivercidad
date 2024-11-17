colores_list = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa", "blanco", "naranja"]

elijo_color = "amarillo"

for color in colores_list:
    print(color)
    if color == elijo_color:
        print(f"color encontrado: {color}")
        break
    else:
        print("color no encontrado")    
     


rango_largo = range(1, 10000)
print(rango_largo)    
for i in rango_largo:
    print(i)
    if i == 3:
        print(f"encontre el: {i}")
        break
        #continue
    else:
        print(f"no encontre el: {i}")   