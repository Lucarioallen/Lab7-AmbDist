from .aspects import add_operation, subtract_operation, multiply_operation, divide_operation

# Funciones genéricas que serán decoradas
def generic_add(a, b):
    pass

def generic_subtract(a, b):
    pass

def generic_multiply(a, b):
    pass

def generic_divide(a, b):
    pass

# Aplicar los decoradores a las funciones genéricas
add = add_operation(generic_add)
subtract = subtract_operation(generic_subtract)
multiply = multiply_operation(generic_multiply)
divide = divide_operation(generic_divide)
