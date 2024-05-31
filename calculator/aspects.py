import logging
import time
from functools import wraps

def tiempo_ejecucion_aspecto(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Tiempo de inicio
        resultado = func(*args, **kwargs)  # Ejecutar el método original
        fin = time.time()  # Tiempo de fin
        tiempo_transcurrido = fin - inicio  # Calcular el tiempo transcurrido
        logging.info(f"Tiempo de ejecución de {func.__name__}: {tiempo_transcurrido} segundos")
        return resultado
    return wrapper

def add_operation(func):
    @wraps(func)
    @tiempo_ejecucion_aspecto
    def wrapper(a, b):
        return a + b
    return wrapper

def subtract_operation(func):
    @wraps(func)
    @tiempo_ejecucion_aspecto
    def wrapper(a, b):
        return a - b
    return wrapper

def multiply_operation(func):
    @wraps(func)
    @tiempo_ejecucion_aspecto
    def wrapper(a, b):
        return a * b
    return wrapper

def divide_operation(func):
    @wraps(func)
    @tiempo_ejecucion_aspecto
    def wrapper(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    return wrapper
