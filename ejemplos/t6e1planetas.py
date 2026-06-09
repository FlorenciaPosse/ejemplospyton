#Lista de planetas
planetas = ["Mercurio","Venus","Tierra","Marte","Júpiter","Saturno","Urano","Neptuno"]

#conversion nº a texto
numero = int(input("Elige un número del 1 al 8 como planetas hay en el sistema SOLAR: "))

#validar que se encuentra dentro del rango 
if numero >= 1 and numero <= 8:
    planeta = planetas[numero - 1]
    print("El planeta que has seleccionado es:", planeta)
    #si el numero introducido es mayor que 8 manda mensaje de error 
else:
    print("¡Numero incorrecto! ¡Solo hay 8 Planetas!.")
