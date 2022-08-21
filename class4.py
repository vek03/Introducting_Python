a = int(input('1° Bim: '))
while a > 10:
    a = int(input('Tente novamente. 1° Bim: '))
b = int(input('2° Bim: '))
while b > 10:
    b = int(input('Tente novamente. 2° Bim: '))
c = int(input('3° Bim: '))
while c > 10:
    c = int(input('Tente novamente. 3° Bim: '))
d = int(input('4° Bim: '))
while d > 10:
    d = int(input('Tente novamente. 4° Bim: '))

media = (a + b + c + d) / 4
print('Sua média é: {}'.format(media))


# a = 0
# while a < 11:
#     print(a)
#     a += 1


# a = int(input('Insira um valor: '))
#
# for i in range(a + 1):
#     div = 0
#     for x in range(1, i+1):
#         rest = i % x
#         #print(i, rest)
#         if rest == 0:
#             div += 1
#
#     if div == 2:
#         print(i)



# print('Números Primos')
# a = int(input('Insira um número: '))
#
# div = 0
#
# for x in range(1, a+1):
#     rest = a % x
#     print(a, rest)
#     if rest == 0:
#         div += 1
#
# if div == 2:
#     print('N° {} é primo',format(a))
# else:
#     print('N° {} não é primo'.format(a))