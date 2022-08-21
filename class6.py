#preferencias:
#lista(list): []
#tupla(tuple): ()
#conjuntos(set): {}
#sets não repetem números


conj1 = {1, 2, 3, 4, 5}
conj2 = {5, 6, 7, 8,}
conj_union = conj1.union(conj2)
print('União: {}'.format(conj_union))
#mesmas regras da matemática
#não repete números, e os une

conj_intersection = conj1.intersection(conj2)
print('Intersecção: {}'.format(conj_intersection))
#intersecção, intersection mostra os nums repetidos

conj_difference1 = conj1.difference(conj2)
print('Diferenças entre 1 e 2: {}'.format(conj_difference1))
#difference, diferença mostra os numeros diferentes do conjunto inicial
conj_difference2 = conj2.difference(conj1)
print('Diferenças entre 2 e 1: {}'.format(conj_difference2))
print('Diferenças entre 2 e 1: {}'.format(conj_difference2))
#mostra os números diferentes do conjunto fora do parametro

conj_diff_simetric = conj1.symmetric_difference(conj2)
print('Diferença simétrica: {}'.format(conj_diff_simetric))

print('')
conj_a = {1, 2, 3}
conj_b = {1, 2, 3, 4, 5}
print('Conjunto A: {}'.format(conj_a))
print('Conjunto B: {}'.format(conj_b))
conj_subset = conj_a.issubset(conj_b)
print('A é subconjunto de B: {}'.format(conj_subset))
#retorna um boolean se o caso é um subconjunto de tal

conj_superset = conj_a.issuperset(conj_b)
print('A é superconjunto de B: {}'.format(conj_superset))
#boolean se o conjunto é superconjunto de tal
print('')

lista = ['cachorro', 'gato', 'cachorro', 'gato']
print(lista)
conj_animals = set(lista)
print(conj_animals)
list_animals = list(conj_animals)
print(list_animals)


# conj = {1, 2, 3, 4, 4, 2}
# conj.add(5)
# conj.discard(2)
# print(conj)