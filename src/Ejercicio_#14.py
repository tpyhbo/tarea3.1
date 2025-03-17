#14 Piensa en al menos 3 animales con características similares y almacénalos en una lista. A) Imprime un mensaje para cada animal. Ejemplo: "Un perro sería un gran amigo." B) Agrega un nuevo animal y luego imprime un mensaje general. Ejemplo: "Todos estos animales serían una gran mascota.".
animeles = ["perro", "gato", "mapache"]
for animal in animeles:
    print(f"Un {animal} sería un gran amigo.\n")
animeles.append("canguro")
print("Todos estos animales serían una gran mascota.")