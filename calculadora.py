class Calculadora: 
    def calcular(self, exp: str):
        return f"Resultado de {exp} = {eval(exp)}"