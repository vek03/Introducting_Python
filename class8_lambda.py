#lambda é função anonima
#mesma função do 8_2, porem mais simplificado

cont_letters = lambda lista: [len(x) for x in lista]

list_animals = ['cachorro', 'gato', 'elefante']
print(cont_letters(list_animals))

soma = lambda a, b: a + b
sub = lambda a, b: a - b

print(soma(5, 10))
print(sub(10, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b : a * b,
    'div': lambda a, b: a / b
}

print(type(calculadora))
soma = calculadora['soma']
mult = calculadora['mult']

print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(mult(15,5)))