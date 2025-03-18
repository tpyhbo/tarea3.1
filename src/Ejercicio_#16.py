#16 Crea un programa que calcule el factorial de un número dado.
num = int(input("Dame un número: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"El factorial de {num} es {fact}.")