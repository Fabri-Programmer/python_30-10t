def suma(x, y):
    print(f"La suma es: {x + y}")
def resta(x, y):
    print(f"La resta es: {x - y}")
def multi(x, y):
    print(f"La multiplicación es: {x * y}")
def divi(x, y):
    if y != 0:
        print(f"La división es: {x / y}")
    else:
        print("Error: División por cero.")

print("BIENVENIDO AL SISTEMA DE FUNCIONES BÁSICAS")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("0. Salir")

while True:
    opcion = input("Ingrese una opción: ")
    
    if opcion == '0':
        print("Saliendo del sistema.")
        break
    elif opcion in ['1', '2', '3', '4']:
        x = float(input("Ingrese el primer número: "))
        y = float(input("Ingrese el segundo número: "))
        if opcion == '1':
            suma(x, y)
        elif opcion == '2':
            resta(x, y)
        elif opcion == '3':
            multi(x, y)
        elif opcion == '4':
            divi(x, y)
    else:
        print("Opción no válida. Intente de nuevo.")
