#color==(igual)mensaje 
def mensaje_color(color):
    color = color.lower()

    if color=="rojo":
         return ("Hoy no vine a pasar desapercibido. Vine a dejar huella, a romper límites y a encender todo lo que toque con mi energía. La pasión no se explica: se siente, se vive y se contagia. Que cada paso tenga fuerza, cada mirada intención y cada sueño el fuego suficiente para hacerse realidad.")
    elif color=="verde":
         return ("La esperanza florece cuando decides no rendirte, y el crecimiento comienza cuando crees en ti.")
    elif color== "azul":
        return ("La calma llega cuando aprendes a respirar paz en medio del ruido.")
    elif color== "amarillo":
        return ("La felicidad comienza cuando decides mirar la vida con esperanza y una sonrisa.")
    elif color== "morado":
        return ("La sabiduría nace de escuchar, y la creatividad de atreverse a imaginar lo que otros no ven.")
    else:
        return "color no seleccionable"

#Pedimos al usuario que un color 

color_seleccionado = input(" ELIGE UN COLOR (Rojo, Verde, Azul, Amarillo, Morado): ")

mensaje = mensaje_color(color_seleccionado)
#imprimimos el color con el mensaje final
print("Color seleccionado", color_seleccionado)
print("Mensaje:", mensaje_color(color_seleccionado))
