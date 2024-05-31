class Calculadora: 
    def calcular(self, exp: str):
        return f"Resultado de {exp} = {eval(exp)}"

print("Calculadora")
calc = Calculadora()
exp = input("digite la expresion: ")
print(calc.calcular(exp))
input("presiona enter para continuar...")