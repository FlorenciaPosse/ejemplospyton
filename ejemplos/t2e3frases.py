#Pedimos al usuario que introduzca una frase
frase = input("Introduce una frase: ")
longitud = len(frase)

#imprimimos la palabra
print(frase)
#imprimir la longitud (al ser un numero no puede ir solo)
print("Longitud de la frase", longitud)
#imprimir cadena en mayusculas
print("La frase en mayusculas es:", frase.upper())
#imprimir la cadena en minusculas
print ("La frase en minusculas es:", frase.lower())