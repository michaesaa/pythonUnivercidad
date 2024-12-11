import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import DateEntry

# Credenciales de usuario y roles
usuarios = {
    "admin": {"password": "123", "rol": "admin"},
    "usuario": {"password": "456", "rol": "usuario"}
}

inventario = []

# Variable para almacenar el rol del usuario actual
rol_actual = None

# Función de inicio de sesión
def iniciar_sesion():
    global rol_actual
    usuario = simpledialog.askstring("Login", "Usuario:")
    contraseña = simpledialog.askstring("Login", "Contraseña:", show="*")
    
    if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
        rol_actual = usuarios[usuario]["rol"]
        messagebox.showinfo("Inicio de sesión", f"¡Inicio de sesión exitoso como {usuario}!")
        ventana_login.destroy()  # Cierra la ventana de login
        abrir_inventario()  # Abre la ventana de inventario
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para abrir la ventana de inventario
def abrir_inventario():
    ventana = tk.Tk()
    ventana.title("Gestión de Inventario - Eco Moda")
    ventana.geometry("400x400")

    # Función para ingresar un producto
    def ingresar_producto():
        producto = entrada_producto.get()
        cantidad = entrada_cantidad.get()
        talla = entrada_talla.get()
        color = entrada_color.get()
        precio = entrada_precio.get()
        fecha = entrada_fecha.get()
        try:
            if producto and cantidad and talla and color and precio and fecha:
            # Convertir cantidad y precio a sus tipos correctos
               cantidad = int(cantidad)
               precio = float(precio)

            # Buscar si el producto ya existe
            producto_existente = None
            for item in inventario:
                if (item[0] == producto and item[2] == talla and
                        item[3] == color and item[4] == precio and
                        item[5] == fecha):
                    producto_existente = item
                    break

            if producto_existente:
                # Si existe, sumar la cantidad
                producto_existente[1] += cantidad
                resultado_label.config(text=f"Cantidad del producto '{producto}' actualizada correctamente.")
            else:
                # Si no existe, agregar como un nuevo producto
                item = [str(producto), cantidad, talla, color, precio, fecha]
                inventario.append(item)
                resultado_label.config(text=f"Producto '{producto}' agregado correctamente.")
            
            resultado_label.config(text="Todos los campos son obligatorios.")
        except ValueError:
            resultado_label.config(text="Algún campo no tiene el formato correcto.")





    # Función para imprimir el inventario
    def imprimir_inventario():
        inventario_texto.delete(1.0, tk.END)
        if inventario:
            texto = "\n".join([f"{idx + 1}. {str(item)}" for idx, item in enumerate(inventario)])
            inventario_texto.insert(tk.END, texto)
        else:
            inventario_texto.insert(tk.END, "El inventario está vacío.")

    # Buscar producto
    def buscar_producto():
        producto = simpledialog.askstring("Buscar Producto", "Ingrese el nombre del producto:")
        coincidencias = [(idx, item) for idx, item in enumerate(inventario) if item[0] == producto]

        if coincidencias:
            texto = "\n".join([f"{idx + 1}. {str(item)}" for idx, item in coincidencias])
            messagebox.showinfo("Resultados de búsqueda", texto)
        else:
            messagebox.showinfo("Resultados de búsqueda", "Producto no encontrado.")

    def modificar_producto():
        try:
            # Solicitar el número del ítem a modificar
            numero_item = simpledialog.askinteger("Modificar Producto", "Ingrese el número del ítem:")
            if numero_item is None or numero_item <= 0 or numero_item > len(inventario):
                messagebox.showerror("Error", "Número de ítem inválido.")
                return

            # Obtener el ítem a modificar
            item_a_modificar = inventario[numero_item - 1]
            nuevo_producto = simpledialog.askstring("Modificar Producto", f"Nuevo nombre ({item_a_modificar[0]}):", initialvalue=item_a_modificar[0])
            nueva_cantidad = simpledialog.askinteger("Modificar Producto", f"Nueva cantidad ({item_a_modificar[1]}):", initialvalue=item_a_modificar[1])
            nueva_talla = simpledialog.askstring("Modificar Producto", f"Nueva talla ({item_a_modificar[2]}):", initialvalue=item_a_modificar[2])
            nuevo_color = simpledialog.askstring("Modificar Producto", f"Nuevo color ({item_a_modificar[3]}):", initialvalue=item_a_modificar[3])
            nuevo_precio = simpledialog.askfloat("Modificar Producto", f"Nuevo precio ({item_a_modificar[4]}):", initialvalue=item_a_modificar[4])
            nueva_fecha = simpledialog.askstring("Modificar Producto", f"Nueva fecha ({item_a_modificar[5]}):", initialvalue=item_a_modificar[5])

            if nuevo_producto and nueva_cantidad and nueva_talla and nuevo_color and nuevo_precio and nueva_fecha:
                # Actualizar el ítem
                inventario[numero_item - 1] = [str(nuevo_producto), int(nueva_cantidad), nueva_talla, nuevo_color, float(nuevo_precio), nueva_fecha]
                messagebox.showinfo("Modificar Producto", f"Producto número {numero_item} modificado con éxito.")
            else:
                messagebox.showerror("Error", "No se realizaron cambios; algún campo está vacío.")
        except ValueError:
            messagebox.showerror("Error", "Error en los datos ingresados.")

    def eliminar_producto():
        try:
            # Solicitar el número de ítem a eliminar
            numero_item = simpledialog.askinteger("Eliminar Producto", "Ingrese el número del ítem:")
            
            # Validación de que el número del ítem sea válido
            if numero_item is None or numero_item <= 0 or numero_item > len(inventario):
                messagebox.showerror("Error", "Número de ítem inválido.")
                return
            
            item_eliminado = inventario.pop(numero_item - 1)
            messagebox.showinfo("Eliminar Producto", f"Producto '{item_eliminado[0]}' eliminado con éxito.")
        except Exception:
            messagebox.showerror("Error", f"Error al eliminar el producto")

    # Limpiar

    def limpia():
        entrada_producto.delete(0,tk.END)
        entrada_cantidad.delete(0,tk.END)
        entrada_color.delete(0,tk.END)
        entrada_talla.delete(0,tk.END)
        entrada_precio.delete(0,tk.END)

    # Interfaz gráfica
    labelproducto = tk.Label(ventana, text="Producto:")
    labelproducto.place(x=20, y=10, width=90, height=20)
    entrada_producto = tk.Entry(ventana)
    entrada_producto.place(x=120, y=10, width=100, height=20)

    labelcantidad = tk.Label(ventana, text="Cantidad:")
    labelcantidad.place(x=20, y=30, width=90, height=20)
    entrada_cantidad = tk.Entry(ventana)
    entrada_cantidad.place(x=120, y=30, width=100, height=20)

    labeltalla = tk.Label(ventana, text="Talla:") 
    labeltalla.place(x=20, y=50, width=90, height=20)
    entrada_talla = tk.Entry(ventana)
    entrada_talla.place(x=120, y=50, width=100, height=20)

    labelcolor = tk.Label(ventana, text="Color:")
    labelcolor.place(x=20, y=70, width=90, height=20)
    entrada_color = tk.Entry(ventana)
    entrada_color.place(x=120, y=70, width=100, height=20)

    labelprecio = tk.Label(ventana, text="Precio:")
    labelprecio.place(x=20, y=90, width=90, height=20)
    entrada_precio = tk.Entry(ventana)
    entrada_precio.place(x=120, y=90, width=100, height=20)

    labelfecha = tk.Label(ventana, text="Fecha de ingreso:")
    labelfecha.place(x=20, y=110, width=90, height=20)
    entrada_fecha = DateEntry(ventana, date_pattern='dd/mm/yy')
    entrada_fecha.place(x=120, y=110, width=100, height=20)

    # Barra de desplazamiento y caja de texto para el inventario
    frame_inventario = tk.Frame(ventana)
    frame_inventario.place(x=20, y=260, width=360, height=100, )

    scroll_inventario = tk.Scrollbar(frame_inventario)
    scroll_inventario.pack(side=tk.RIGHT, fill=tk.Y)

    inventario_texto = tk.Text(frame_inventario, wrap=tk.WORD, yscrollcommand=scroll_inventario.set, font=("Arial",10))
    inventario_texto.pack(expand=True, fill=tk.BOTH)

    scroll_inventario.config(command=inventario_texto.yview)

    # Label de resultado
    resultado_label = tk.Label(ventana, text="", fg="blue", anchor="w")
    resultado_label.place(x=20, y=370, width=360, height=20)

    # Botones según el rol
    if rol_actual == "admin":
        tk.Button(ventana, text="Ingresar Producto", command=ingresar_producto, background="#00ff04").place(x=240, y=30, width=110, height=25)
        tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto, background="#ff0000").place(x=240, y=70, width=110, height=25)
        tk.Button(ventana, text="Buscar Producto", command=buscar_producto, background="#00ffb9").place(x=125, y=170, width=150, height=20)
        tk.Button(ventana, text="Modificar Producto", command=modificar_producto, background="#00ffb9").place(x=125, y=200, width=150, height=20)

    elif rol_actual == "usuario":
        tk.Button(ventana, text="Ingresar Producto", command=ingresar_producto, background="#00ff04").place(x=240, y=30, width=110, height=25)

    tk.Button(ventana, text="Imprimir Inventario", command=imprimir_inventario, background="#00ffb9").place(x=125, y=230, width=150, height=20)

    tk.Button(ventana, text="Limpiar", command=limpia, background="#00ffb9").place(x=240, y=110, width=110, height=25)

    ventana.mainloop()

# Ventana de login
ventana_login = tk.Tk()
ventana_login.title("Login - Eco Moda")
ventana_login.geometry("300x200")

# Label del login
tk.Label(ventana_login, text="Bienvenid@, Por favor inicie sesión.").pack(pady=20)
tk.Button(ventana_login, text="Iniciar Sesión", command=iniciar_sesion).pack(pady=20)

ventana_login.mainloop()