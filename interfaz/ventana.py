from tkinter import *

def click():
    
    texto = "hola,"+ entrada.get()
    etiqueta.configure(text=texto)

# VENTANA PRINSIPAL
ventana = Tk()
ventana.title("prueba")
ventana.resizable(True, True)
ventana.config()

# VENTANA SEGUNDARIA
frame = Frame()
frame.pack()
frame.config(bg="blue")
frame.config(width="400", height="400")

# PARA AGREGAR TEXTO  Label
etiqueta = Label(frame, text="Esto es una prueba", font="Arial 20")
etiqueta.grid(column=1, row=2 )

# para agreagar un botton   Button

boton = Button(
    frame,
    text="oprimeme", 
    bg="red",
    fg="black",
    command=click
    )
boton.grid(column=1, row=4)


#para agregar cuadro de texto  Entry
entrada = Entry(frame,width=50)
entrada.grid(column=2, row=2)


# etiqueta2 = Label(frame, text="Etiqueta2")
# etiqueta2.grid(row=2, column=2)

# etiqueta.pack() 
# pack es para colocar el label en el frame
# y para acomodar la posicion del label .place(x=0, y=0)
ventana.mainloop()
