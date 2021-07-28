# Aprendendo a utilizar  tratamento e customizar exceções

# try:
# #Erro de divisão por zeros de
#     divisao = 10 / 0
# except ZeroDivisionError: #Filho
# #except ArithmeticError: #PAI
#     print('Não é possivel realizar divisão por zero')

# lista = [1,10]
# try:
# #list index out of range
#     divisao = 10 / 1
#     numero = lista[3]
# except: #Só except para tratamento genéricode erro
#     print('Erro desconhecido')

# lista = [1,10]
# try:
# #list index out of range
#     divisao = 10 / 1
#     numero = lista[3]
# except IndexError:
#     print('Erro ao acessar um indice inválido da Lista')

lista = [1,10]
arquivo = open('notas.txt', 'r')

try:
    texto = arquivo.read()
# Variável inexistente
    divisao = 10 / 1
    numero = lista[1]

except IndexError:
    print('Erro ao acessar um indice inválido da Lista')
#except BaseException as ex: #É o pai das exeçoes (para tratar erros não previstos)
except Exception as ex:  # É o pai das exeçoes (para tratar erros não previstos)

    print("Erro desconhecido. Erro {}".format(ex))
else: #Executa mais cpodigo qnd  ocorre exceção
    print('Executa qnd não ocorre exceção')
finally: #Sempre executa
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()