#color==(igual)mensaje 
def mensaje_color(color):
    color = color.lower()

    if color=="rojo":
         return ("mensaje de pasión y energía")
    elif color=="verde":
         return ("mensaje de esperanza y crecimiento")
    elif color== "azul":
        return ("mensaje de calma y serenidad")
    elif color== "amarillo":
        return ("mensaje de felicidad y optimismo")
    elif color== "morado":
        return ("mensaje de sabiduria y creatividad")
    else:
        return "color no seleccionable"

#Pedimos al usuario que un color 

color_seleccionado = input(" ELIGE UN COLOR (Rojo, Verde, Azul, Amarillo, Morado): ")

mensaje = mensaje_color(color_seleccionado)
#imprimimos el color con el mensaje final
print("Color seleccionado", color_seleccionado)
print("Mensaje:", mensaje_color(color_seleccionado))