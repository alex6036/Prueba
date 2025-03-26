def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def main():
    while True:
        try:
            n = int(input("Ingrese el número de términos de la secuencia de Fibonacci que desea ver (0 para salir): "))
            if n == 0:
                print("Saliendo del programa.")
                break
            elif n < 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                print(f"Secuencia de Fibonacci con {n} términos: {fibonacci(n)}")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

if __name__ == "__main__":
    main()