#13 Crea una lista con tus pizzas favoritas (al menos 3 elementos): A) Imprime un mensaje para cada tipo de pizza. Ejemplo: "Me gusta la pizza de pepperoni." B) Añade un nuevo elemento a la lista después del for e imprímelo. Ejemplo: "Me gusta mucho la pizza de champiñones.".
pizzas = ["pepperoni", "piña", "4 quesos"]
for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza}.\n")
pizzas.append("champiñones")
print(f"Me gusta mucho la pizza de {pizzas[3]}.")