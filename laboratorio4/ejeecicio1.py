import tkinter as tk

def incrementar():
    numero = int(campo_texto.get())
    campo_texto.delete(0, tk.END)
    campo_texto.insert(0, str(numero + 1))

def decrementar():
    numero = int(campo_texto.get())
    campo_texto.delete(0, tk.END)
    campo_texto.insert(0, str(numero - 1))

ventana = tk.Tk()
ventana.title("Incrementar/Decrementar")

campo_texto = tk.Entry(ventana, width=10, justify='center')
campo_texto.insert(0, "0")
campo_texto.grid(row=0, column=1)

btn_incrementar = tk.Button(ventana,
text="+",
command=incrementar)
btn_incrementar.grid(row=1, column=2)

btn_decrementar = tk.Button(ventana, text="-", command=decrementar)
btn_decrementar.grid(row=1, column=0)

ventana.mainloop()
