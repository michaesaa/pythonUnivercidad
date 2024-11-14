import tkinter as tk 

def saludar():
    saludo.set("hola" + txtnombre.get())


app = tk.Tk()
app.geometry("600x300")
# resultado = tk.StringVar()
# mostrar resultados
# se define la variable para enlazar cone el labelsaludo 
saludo = tk.StringVar()

labelnombre = tk.Label(
    text="Nombre"
)

labelnombre.place(x=10,y=10,width=50,height=25)
# labelnombre.pack()


txtnombre =tk.Entry(
    app,
)


txtnombre.place(x=110,y=10,width=50,height=25)

button = tk.Button(
    app,
    text="saludar",
    bg="red",
    fg="white",
    command=saludar
)

button.place(x=60,y=50,width=50,height=25)

labelsaludo = tk.Label(
    app,
    textvariable=saludo

)

labelsaludo.place(x=200,y=10,width=100,height=25)




app.mainloop()




