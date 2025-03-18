#15 Usando list comprehension, crea: Una lista con solo números pares (sin usar range). Otra lista que almacene los números impares (el usuario elige los números).
def lista_pares(n, m):
    if n > m:
        return []
    elif n % 2 == 0:
        return [n] + lista_pares(n + 1, m)
    else:
        return lista_pares(n + 1, m)

def lista_impares(n, m):
    if n > m:
        return []
    elif n % 2 != 0:
        return [n] + lista_impares(n + 1, m)
    else:
        return lista_impares(n + 1, m)

print("Dame un rango de números.")
x = int(input("Número 1: "))
y = int(input("Número 2: "))
if x > y:
    print("El primer número debe ser menor o igual al segundo.")
else:
    print("""
    Dime qué lista deseas ver.
    1. Pares
    2. Impares
    """)
opc = int(input("Opción: "))
if opc == 1:
    print(lista_pares(x, y))
elif opc == 2:
    print(lista_impares(x, y))
else:
    print("Opción no válida.")