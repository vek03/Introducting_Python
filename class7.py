#método: não tem retorno
#função: tem retorno
#classe:

class Calculadora:
    def __init__(self, num1, num2): #metodo principal que sempre será iniciado
        self.a = num1 #self é this, referencia a classe
        self.b = num2

    def soma(self): #parametro pq ele necessita sempre receber esses valores
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

calc = Calculadora(10, 2)
print('A= {}'.format(calc.a))
print('B= {}'.format(calc.b))
print('Soma: {}'.format(calc.soma()))
print('Subtração: {}'.format(calc.sub()))
print('Multiplicação: {}'.format(calc.mult()))
print('Divisão: {}'.format(calc.div()))