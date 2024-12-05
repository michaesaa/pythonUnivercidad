import tkinter as tk
from math import factorial

def calcular_factorial():
    try:
        numero = int(entry_numero.get())  
        if numero < 0:
            entry_resultado.delete(0, tk.END)
            entry_resultado.insert(0, "Error: Negativo")
        else:
            resultado = factorial(numero) 
            entry_resultado.delete(0, tk.END)
            entry_resultado.insert(0, str(resultado))  
    except ValueError:
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Factorial")
ventana.geometry("300x200")

# Etiqueta y campo para ingresar el número
tk.Label(ventana, text="Número:").pack(pady=5)
entry_numero = tk.Entry(ventana, width=20)
entry_numero.pack()

# Botón para calcular el factorial
btn_calcular = tk.Button(ventana, text="Siguiente", command=calcular_factorial)
btn_calcular.pack(pady=10)

# Etiqueta y campo para mostrar el resultado
tk.Label(ventana, text="Factorial:").pack(pady=5)
entry_resultado = tk.Entry(ventana, width=20)
entry_resultado.pack()

# Inicia el bucle principal de la ventana
ventana.mainloop()
