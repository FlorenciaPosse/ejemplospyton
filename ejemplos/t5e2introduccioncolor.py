#creamos el bucle con for ya que se puede elegir el color 5 veces 
for i in range(5):
    color = input("Introduce un color: ")
    #da igual como se intruduzca el color que lo convertira a minusculas
    color = color.lower()

    if color == "azul":
        print(" ¡Premio! Has acertado el color.")
        #break para parar el bucle
        break
    else:
        print("¡Color no ganador!, prueba otro.")