import tkinter as tk

# Funciones para las operaciones
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, str(resultado))
    except ValueError:
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, str(resultado))
    except ValueError:
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, str(resultado))
    except ValueError:
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            entry_resultado.delete(0, tk.END)
            entry_resultado.insert(0, "Error: Div/0")
        else:
            resultado = num1 / num2
            entry_resultado.delete(0, tk.END)
            entry_resultado.insert(0, str(resultado))
    except ValueError:
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")

def limpiar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_resultado.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Primer número:").grid(row=0, column=0, pady=5, padx=5)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, pady=5, padx=5)

tk.Label(ventana, text="Segundo número:").grid(row=1, column=0, pady=5, padx=5)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, pady=5, padx=5)

tk.Label(ventana, text="Resultado:").grid(row=2, column=0, pady=5, padx=5)
entry_resultado = tk.Entry(ventana)
entry_resultado.grid(row=2, column=1, pady=5, padx=5)

# Botones para operaciones
tk.Button(ventana, text="+", command=sumar).grid(row=3, column=0, pady=5, padx=5)
tk.Button(ventana, text="-", command=restar).grid(row=3, column=1, pady=5, padx=5)
tk.Button(ventana, text="*", command=multiplicar).grid(row=4, column=0, pady=5, padx=5)
tk.Button(ventana, text="/", command=dividir).grid(row=4, column=1, pady=5, padx=5)

# Botón para limpiar los campos
tk.Button(ventana, text="CLEAR", command=limpiar).grid(row=5, column=0, columnspan=2, pady=10, padx=5)

# Inicia el bucle principal de la ventana
ventana.mainloop()
