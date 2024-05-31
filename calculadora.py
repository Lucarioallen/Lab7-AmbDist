class Calculadora: 
    def calcular(self, exp: str):
        return f"Resultado de {exp} = {eval(exp)}"

def main():
    print("Calculadora")
    calc = Calculadora()
    try:
        exp = input("digite la expresion: ")
        print(calc.calcular(exp))
        input("presiona enter para continuar...")
    except Exception as e:
        print("error en la expresion")
        main()
   