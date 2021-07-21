# Funçaõ conta palavras

def contador_letras(lista_palavras):
    cont = []
    for x in lista_palavras:
        qtd = len(x)
        cont.append(qtd)
    return cont

def teste():
    return "Teste"
if __name__ == '__main__':
    lista_palavras = ['cachorro', 'gato', 'tamanduá']

    print(contador_letras(lista_palavras))
