#definimos la variable nota_media
def nota_media():
    cantidad = int(input("¿Cuántas notas deseas introducir?: "))

    suma = 0
#usamos for para saber cuantas veces repetimos algo
    for i in range(cantidad):
        nota = float(input(f"Introduce la nota {i + 1}: "))
        suma = suma + nota
#definimos que es la media 
    media = suma / cantidad

    return media
#resultado final de las notas introducidas entre la cantidad = media 

resultado = nota_media()

print("La nota media es:", resultado)