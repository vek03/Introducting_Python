def cont_letters(list_words):
    cont = []
    for x in list_words:
        quant = len(x)
        cont.append(quant)
    return cont

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(cont_letters(lista))