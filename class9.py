import shutil

def write_archive(text):
    diretorio = 'C:/Users/PC GAMER/PycharmProjects/appPython/notas.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(text)
    arquivo.close()

def update_archive(name_archive, text):
    arquivo = open(name_archive, 'a')
    arquivo.write(text)
    arquivo.close()

def read_archive(name_archive):
    arquivo = open(name_archive, 'r')
    text = arquivo.read()
    print(text)

def read_media(name_archive):
    arquivo = open(name_archive, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') #toda vez que encontrar tal, insere na lista
    #print(aluno_nota)
    list_media = []
    for x in aluno_nota:
        list_notas = x.split(',')
        aluno = list_notas[0]
        list_notas.pop(0)
        print(aluno)
        print(list_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(list_notas))
        list_media.append({aluno: media(list_notas)})
    return list_media

def copy_archive(name_archive):
    shutil.copy(name_archive, 'C:/Users/PC GAMER/Documentos/notas_alunos.txt')

def move_archive(name_archive):
    shutil.move(name_archive, 'C:/Users/PC GAMER/Downloads/notas_alunos.txt')

if __name__ == '__main__':
     write_archive('')
     aluno = 'oioi: 5, 5, 5, 5\n'
     update_archive('notas.txt', aluno)
     copy_archive('notas.txt')
     move_archive('notas.txt')
     #list_media = read_media('notas.txt')
     #print(list_media)
     #aluno = 'oioi: 5, 5, 5, 5\n'
     #update_archive('notas.txt', aluno)
     #read_archive('teste.txt')