# Gere, copie, mova, escreva e leia informações de arquivos externos
import shutil

diretorio = '/home/sony/WorkSpace/capacitacao_dataEnginner_DIO_at_GITHUB/cursos/arquivo_de_Teste_Aula_09_DIO.txt'

def escrever_arquivo(texto):
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)

        media_notas = lambda notas: sum([int(i) for i in notas])/4

        print(media_notas(lista_notas))
        lista_media.append({aluno:media_notas(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/sony/WorkSpace/capacitacao_dataEnginner_DIO_at_GITHUB/cursos/notas_copy.txt')

def move_arquivos(nome_arquivo):
    shutil.move(nome_arquivo, '/home/sony/WorkSpace/capacitacao_dataEnginner_DIO_at_GITHUB/cursos')

#Escrever, atualizar e ler arquivo
if __name__ == '__main__':
    #move_arquivos('teste.txt')
    #copia_arquivo('notas.txt')
    lista_media = media_notas('notas.txt')
    #print(lista_media)
    #aluno = '\nCesar, 6, 8, 6, 9'
    #escrever_arquivo('Primeira Linha.\n')
    #atualizar_arquivo("Terceira Linha.\n")
    #atualizar_arquivo('notas.txt', aluno)