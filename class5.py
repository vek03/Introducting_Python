list_num = [12, 10, 7, 5]
list_animals = ['gato', 'elefante', 'cachorro', 'alpha', 'rato', 'baleia']

list_animals[0] = 'macaco'
print(list_animals)
#altera a lista

tupla = (1, 10, 12, 14)
print(tupla[2])
#tuplas tem objetos imutaveis, diferente da list
print(len(tupla))
#mostra quantos itens tem

tupla_animals = tuple(list_animals)
print(tupla_animals)
#converter list em tupla

list_num = list(tupla)



# list_num.sort()
# list_animals.sort()
# print(list_animals)
# print(list_num)
# #reodena a lista de acordo com tamanhos se for int ou por alfabetica se for str
#
# list_animals.reverse()
# print(list_animals)
#ordena a lista em ordem decrescente, int ou str

# print(list_animals[1])
#
# if 'lobo' in list_animals:
#      print('existe um lobo')
# else:
#      print('não existe um lobo')
#      list_animals.append('lobo')
#      # adiciona um item a lista
#      print(list_animals)

# list_animals.pop()
# #tira o ultimo item da lista se vazio, ou tira o item q for especificado
# print(list_animals)

# list_animals.remove('elefante')
# #remove um elemento especifico
# print(list_animals)

# new_list = list_animals * 3
# print(new_list)
# repete os valores da lista por 3 na nova
#
# if 'gato' in list_animals:
#     print('existe um gato')
# else:
#     print('não existe um gato')

# print(max(list_animals))
#busca por ordem alfabética

# print(min(list_num))
# print(max(list_num))
# print(sum(list_num))

# soma = 0
# for x in list_num:
#     print(x)
#     soma += x
# print(soma)