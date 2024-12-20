def calculadora(num1,num2,operacion='multiplicar'):
    def sumar(num1,num2):
        return num1 * num2
    def restar(num1,num2):
        return num1 - num2
    def dividir(num1,num2):
        return num1 / num2
    def multiplicar(num1,num2):
        return num1 * num2
    if operacion == 'sumar':
        print(f'{num1} + {num2} = {sumar(num1,num2)}') 
    elif operacion == 'restar':
          print(f'{num1} - {num2} = {restar(num1,num2)}') 
    elif operacion == 'dividir':
          print(f'{num1} / {num2} = {dividir(num1,num2)}') 
    elif operacion == 'multiplicar':
          print(f'{num1} * {num2} = {multiplicar(num1,num2)}') 

print(calculadora(8,8))   
print(calculadora(4,2,'multiplicar')) 
print(calculadora(9,3,'restar'))