global name
# Componente "Saludo"
def saludar(nombre):
  print(f"Hola, {nombre}!")

def get_name():
  return name

def main():
  global name
  print("Componente Saludo")
  nombre = input("Ingrese su nombre: ")
  name=nombre
  saludar(nombre)
  input("presiona enter para continuar...")
