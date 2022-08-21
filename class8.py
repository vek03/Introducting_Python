#módulo: um arquivo .py
#ex: class8.py

from class7_2 import Televisao
from class7_1 import Calculadora
from class8_1 import cont_letters

tv = Televisao()
print(tv.ligada)
tv.power()
print(tv.ligada)

calc = Calculadora(5, 10)
print(calc.soma())

lista = ['cachorro', 'gato', 'elefante']
total_letters = cont_letters(lista)
print('Total de letras por palavra da lista: {}'.format(total_letters))