#17 Haz un programa que determine si dos palabras son anagramas.
p1 = input("Ingresa la primera palabra: ")
p2 = input("Ingresa la segunda palabra: ")
if sorted(p1.lower()) == sorted(p2.lower()):
    print("Las palabras son anagramas.")
else:
    print("Las palabras no son anagramas.")