#datos que introducimos
precio_camiseta = 10
precio_sudadera = 20.5
precio_gorra = 5.5

numero_camiseta= int (input("¿Que cantidad de camisetas quieres? "))
numero_sudadera = int(input("¿Que cantidad de sudaderas quieres? "))
numero_gorra = int(input("¿Que cantidad de gorras quieres? "))

#sin IVA
total= (
precio_camiseta* numero_camiseta +
precio_sudadera* numero_sudadera +
precio_gorra* numero_gorra
)
#con el 21% IVA
precio_Totalconiva = total * 1.21

print("Total sin IVA:", total, "euros")
print("Precio final con IVA:", round(precio_Totalconiva, 2), "euros")