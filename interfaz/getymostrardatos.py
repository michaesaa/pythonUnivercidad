from tkinter import *

ventana = Tk()
ventana.title("Posicion de ventana")
# ventan.iconbitmap("logo.ico")
# ventana.geometry("400x400")
ventana.resizable(True, True)
ventana.config(bg="red")

frame = Frame()
frame.pack(side="rigth", anchor="s")
frame.config(bg="blue")
frame.config(width="640", height="350")


ventana.mainloop()
