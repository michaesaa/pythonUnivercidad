dias =list(["lunes","martes","miercoles","jueves","viernes","sabado","domingo"])
temperatura=list()

for i in range(len(dias)):
     temp = float(input("ingrese la temperatura" + dias[i]))
     temperatura.append(temp)

for i in range(len(dias)):
     print(dias[i].temperatura[i])      

mayor = max(temperatura)

menor = min(temperatura)

suma = 0

for i in range(len(temperatura)):
     suma = suma+temperatura[i]

promedio = suma /len(temperatura)
print("promedio de temperatura:" + str(promedio))

