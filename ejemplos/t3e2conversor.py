#convertir texto en unidades decimales 
euros = float(input("Introduce tu cantidad en €: "))
#definimos las variables 
cambio_dolares= 1.1
cambio_libras= 0.87
cambio_pesoargentino= 1672.59
#realizamos la multiplicacion
dolares = euros * cambio_dolares
libras= euros* cambio_libras
pesosArgentinos = euros* cambio_pesoargentino
#imprimimos los resultados
print("La cantidad en $ es:", dolares)
print("La cantidad en £ es:", libras)
print("La cantidad en pesos Argentinos es:",pesosArgentinos)