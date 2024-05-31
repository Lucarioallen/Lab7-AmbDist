import threading
import random

# Función para estimar π utilizando hilos
def monte_carlo():
    # Variable compartida para almacenar el número total de puntos dentro del círculo
    num_points = int(input("Ingrese el número total de puntos a generar: "))
    num_threads = 10
    total_points_inside_circle = 0

    # Función que será ejecutada por cada hilo
    def monte_carlo_thread(num_points):
        nonlocal total_points_inside_circle
        
        points_inside_circle = 0
        
        for _ in range(num_points):
            # Generar coordenadas x e y aleatorias en el rango [-1, 1]
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            
            # Calcular la distancia al origen
            distance = x**2 + y**2
            
            # Si la distancia es menor o igual a 1, el punto está dentro del círculo
            if distance <= 1:
                points_inside_circle += 1
        
        # Agregar el número de puntos dentro del círculo al total compartido
        with threading.Lock():
            total_points_inside_circle += points_inside_circle

    threads = []
    
    # Dividir el número total de puntos entre el número de hilos
    points_per_thread = num_points // num_threads
    
    # Crear y ejecutar cada hilo
    for _ in range(num_threads):
        thread = threading.Thread(target=monte_carlo_thread, args=(points_per_thread,))
        thread.start()
        threads.append(thread)
    
    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()
    
    # Calcular la estimación de π basada en el total de puntos dentro del círculo
    pi_estimate = 4 * total_points_inside_circle / num_points

    print("El estimado del valor de PI con el método de Montecarlo, usando ", num_points ," es de : ", pi_estimate)

