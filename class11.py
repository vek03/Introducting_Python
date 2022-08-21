
#existe uma hierarquia nos erros, por isso, coloque na ordem certa
#ou seja, sempre coloque os erros filhos primeiro, para especificar melhor
lista = [1, 10]
try:
    div = 10 / 1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indíce inválido da lista')
except BaseException as ex: #todo erro é dessa classe
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre excessão, ou seja, somente se o try não tiver nenhum erro')
finally:
    print('Sempre executa, independente de dar erro ou não')
    print('Executando restante do codigo...')