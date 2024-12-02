import tkinter as tk

def calcular_iva():
    try:
        precio = float(entry_precio.get())
        iva = precio * 0.19  
        precio_final = precio + iva
        entry_precio_con_iva.delete(0, tk.END)
        entry_precio_con_iva.insert(0, f"{precio_final:.2f}")
    except ValueError:
        entry_precio_con_iva.delete(0, tk.END)
        entry_precio_con_iva.insert(0, "Error")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de IVA")
ventana.geometry("300x200")

# Etiqueta y campo para ingresar el precio
tk.Label(ventana, text="Precio del producto:").pack(pady=5)
entry_precio = tk.Entry(ventana, width=20)
entry_precio.pack()

# Botón para calcular el precio con IVA
btn_calcular = tk.Button(ventana, text="Calcular IVA", command=calcular_iva)
btn_calcular.pack(pady=10)

# Etiqueta y campo para mostrar el precio con IVA
tk.Label(ventana, text="Precio con IVA:").pack(pady=5)
entry_precio_con_iva = tk.Entry(ventana, width=20)
entry_precio_con_iva.pack()

# Inicia el bucle principal de la venta
