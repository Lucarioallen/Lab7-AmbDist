
# Componente "Saludo"
def saludar(nombre):
  print(f"Hola, {nombre}!")

while True:
  print("Componente Saludo")
  nombre = input("Ingrese su nombre: ")
  saludar(nombre)
  input("presiona enter para continuar...")
  break
