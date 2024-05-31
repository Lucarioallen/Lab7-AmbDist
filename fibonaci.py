import threading
import time
import subprocess

# Inicializar los valores iniciales de la secuencia de Fibonacci
fib1 = 0
fib2 = 1

# Crear un bloqueo para sincronizar el acceso a los valores compartidos
lock = threading.Lock()

# Función para calcular la secuencia de Fibonacci usando el primer valor
def fibonacci_thread_1(count):
    global fib1, fib2
    if count == 0:
        time.sleep(1)
    if count == 1:
        time.sleep(1)
        print(fib1 * "🐰", " = ", fib1)
    elif count > 0:
        time.sleep(0.5)
        print(fib1 * "🐰", " = ", fib1)
        for _ in range((count - 1) // 2):  # Cada hilo hará la mitad de los cálculos
            time.sleep(1)  # Simulación de tiempo
            with lock:
                fib1 = fib1 + fib2
                print(fib1 * "🐰", " = ", fib1)

# Función para calcular la secuencia de Fibonacci usando el segundo valor
def fibonacci_thread_2(count):
    global fib1, fib2
    if count == 0:
        time.sleep(1)
    elif count == 2:
        time.sleep(1.1)
        print(fib2 * "🐰", " = ", fib2)
    else:
        for _ in range(count // 2):  # Cada hilo hará la mitad de los cálculos
            time.sleep(1)  # Simulación de tiempo
            with lock:
                fib2 = fib1 + fib2
                print(fib2 * "🐰", " = ", fib2)

# Función que encapsula toda la funcionalidad
def fibonaci():
    # Función para ejecutar el script de la calculadora
    num_elements = int(input("Ingrese el número de elementos de la secuencia de Fibonacci que desea calcular: "))
    # Medir el tiempo de ejecución
    start_time = time.time()

    # Crear los hilos para la secuencia de Fibonacci
    thread1 = threading.Thread(target=fibonacci_thread_1, args=(num_elements,))
    thread2 = threading.Thread(target=fibonacci_thread_2, args=(num_elements,))

    # Crear el hilo para ejecutar el script de la calculadora

    # Iniciar los hilos
    thread1.start()
    thread2.start()

    # Unir los hilos para esperar a que terminen
    thread1.join()
    thread2.join()

    end_time = time.time()
    print("Tiempo de ejecución con hilos:", end_time - start_time, "segundos")

    # Solicitar el número de elementos de la secuencia de Fibonacci a calcular
