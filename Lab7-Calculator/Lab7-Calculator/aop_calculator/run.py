import sys
import os

import logging

# Configuración básica del registro
logging.basicConfig(level=logging.INFO)

# Agregar la ruta del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from calculator import add, subtract, multiply, divide

def main():
    print("Ingrese dos números separados por un espacio:")
    a, b = map(float, input().split())

    print(f"Add: {a} + {b} = {add(a, b)}")
    print(f"Subtract: {a} - {b} = {subtract(a, b)}")
    print(f"Multiply: {a} * {b} = {multiply(a, b)}")
    print(f"Divide: {a} / {b} = {divide(a, b)}")

    # Prueba de manejo de errores
    try:
        divide(a, 4)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()