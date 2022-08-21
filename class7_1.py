#método: não tem retorno
#função: tem retorno
#classe: representa um objeto e seus metodos e funções

class Calculadora:
    def __init__(self, num1, num2): #metodo principal que sempre será iniciado
        self.a = num1
        self.b = num2

    def soma(self): #parametro pq ele necessita sempre receber esses valores
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

print(__name__)
if __name__ == '__main__':
    calc = Calculadora(1, 10)
    print('Soma: {}'.format(calc.soma()))
    print('Subtração: {}'.format(calc.sub()))
    print('Multiplicação: {}'.format(calc.mult()))
    print('Divisão: {}'.format(calc.div()))