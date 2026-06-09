#Pedimos al usuario que introduzca el email
email= input("Introduce tu email: ")
longitud = len(email)

#imprimimos la palabra
print(email)
#imprimir la longitud (al ser un numero no puede ir solo)
print("Longitud del email", longitud)
#imprimir cadena en mayusculas
print("El Email en mayusculas es:", email.upper())
#imprimir la cadena en minusculas
print ("El Email en minusculas es:", email.lower())