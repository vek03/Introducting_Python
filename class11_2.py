
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True: #enquanto verdade for verdade, execute
    try:
        x = int(input('Entre com um valor de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10') #força uma excessão
        elif x < 0:
            raise InputError('Nota não pode ser menor que 10')
        break #força parada do laço após a excessão dar certo
    except ValueError:
        print('Valor inválido. Digite um numero')
    except InputError as ex:
        print(ex)