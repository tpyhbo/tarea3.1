#18 Realiza un programa que imprima la serie de Fibonacci hasta un número dado.
a = 0
b = 1
num = int(input("Ingresa un número hasta el cual deseas ver la serie de Fibonacci: "))
for i in range(num):
    if i == 0:
        print(a)
    elif i == 1:
        print(b)
    else:
        x = a + b
        print(x)
        a = b
        b = x