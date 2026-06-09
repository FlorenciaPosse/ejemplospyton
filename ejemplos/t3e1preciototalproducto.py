nombre = input("Producto: ")
precio = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento (%): "))

# Descuento
def con_descuento(precio, cantidad, desc):
    return precio * cantidad * (1 - desc / 100)

# suma del  IVA
def con_iva(total):
    return total * 1.21


total_desc = con_descuento(precio, cantidad, descuento)
total_final = con_iva(total_desc)

# Total
print("\nProducto:", nombre)
print("Total con descuento:", round(total_desc, 2))
print("Total con IVA:", round(total_final, 2))