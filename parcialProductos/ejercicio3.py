productos = []
inventarios = []

for i in range(3):  # productos
    producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    inventario = int(input(f"Ingrese el inventario de {producto}: "))
    productos.append(producto)
    inventarios.append(inventario)

# productos
for i, producto in enumerate(productos):
    print(f"{producto}: {inventarios[i]} unidades")

# Productos con inventario inferior a 5
bajo_inventario = [productos[i] for i in range(len(inventarios)) if inventarios[i] < 5]
print("Productos con inventario inferior a 5:", bajo_inventario)

# Buscar producto
buscar = input("Ingrese el nombre del producto a buscar: ")
if buscar in productos:
    index = productos.index(buscar)
    print(f"{buscar} tiene {inventarios[index]} unidades.")
else:
    print("Producto no encontrado.")

# Producto con mayor 
max_inventario = max(inventarios)
max_index = inventarios.index(max_inventario)
print(f"El producto con mayor inventario es {productos[max_index]} con {max_inventario} unidades.")
