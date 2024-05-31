class SumaAgente:
    def operar(self, a, b):
        return a + b
 
class RestaAgente:
    def operar(self, a, b):
        return a - b
 
class Calculadora:
    def __init__(self):
        self.agentes = {
            'sumar': SumaAgente(),
            'restar': RestaAgente()
        }
 
    def calcular(self, operacion, a, b):
        agente = self.agentes.get(operacion)
        if agente:
            return agente.operar(a, b)
        else:
            return f"Operación '{operacion}' no soportada."
 
def main():
    calculadora = Calculadora()
    while True:
        operacion = input("Ingrese la operación (sumar/restar) o 'salir' para terminar: ").strip().lower()
        if operacion == 'salir':
            break
        if operacion not in calculadora.agentes:
            print(f"Operación '{operacion}' no soportada. Intente nuevamente.")
            continue
       
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese números válidos.")
            continue
 
        resultado = calculadora.calcular(operacion, a, b)
        print(f"Resultado: {resultado}")
 
if __name__ == "__main__":
    main()