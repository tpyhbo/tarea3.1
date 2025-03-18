#19 Realiza un programa que determine si un número es primo o no.
num = int(input("Ingresa un número: "))
if num <= 1:
    print("El número no es primo.")
elif num == 2:
    print("El número es primo.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("El número no es primo.")
            break
    else:
        print("El número es primo.")