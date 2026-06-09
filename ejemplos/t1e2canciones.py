#Datos de tu cancion favorita

cancion_favorita = input("Cual es tu cancion favorita? ")

artista_cancion = input("Quien es el artista? ")

album_cancion = input("A que album pertenece? ")

año_lanzamiento = input("En que año se lanzo la cancion? ")

duration_minutos = input("Cuantos minutos dura? ")

videoclip_cancion = input("Tiene videoclip? (si/no): ").lower() == "si"

#Datos de tu cancion  menos favorita

cancion_menosfavorita = input("Cual es tu cancion menos favorita? ")

artista_cancionmenos = input("Quien es el artista? ")

album_cancionmenos = input("A que album pertenece? ")

año_lanzamientomenos = input("En que año se lanzo la cancion? ")

duration_minutosmenos = input("Cuantos minutos dura? ")

videoclip_cancionmenos = input("Tiene videoclip? (si/no): ").lower() == "si"

print("Mi cancion favorita es:", cancion_menosfavorita)

print("El artista es:", artista_cancionmenos)

print("Pertenece al album:", album_cancionmenos)

print("Se lanzo en:",año_lanzamientomenos)

print("La cancion dura:", duration_minutosmenos)

print("Tiene videoclip:", videoclip_cancionmenos)