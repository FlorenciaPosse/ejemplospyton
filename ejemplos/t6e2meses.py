#Lista de meses
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

#conversion nº a texto
numero = int(input("Elige un número del 1 al 12 como meses hay en el Año: "))

#validar que se encuentra dentro del rango 
if numero >= 1 and numero <= 12:
   meses = meses[numero - 1]
   print("El mes seleccionado es:",meses)
    #si el numero introducido es mayor que 12 manda mensaje de error 
   if numero==6:
      print ("sin duda es el mejor MES!!")
else:
    print("¡Numero incorrecto! ¡Solo hay 12 meses!.")
    