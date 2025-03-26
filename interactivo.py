def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

if __name__ == "__main__":
    try:
        numero = int(input("Introduce un número para calcular su factorial: "))
        print(f"El factorial de {numero} es {factorial(numero)}")
    except ValueError:
        print("Por favor, introduce un número entero válido.")