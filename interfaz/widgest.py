from tkinter import *

ventana = Tk()
ventana.title("Widgets Basicos")
# ventana.geometry("400x400")
ventana.resizable(True, True)
ventana.config(bg="red")

frame = Frame()
frame.pack(side="left")
frame.config(bg="blue")
frame.config(width="400", height="400")


ventana.mainloop()
