# Trabalhando com a função lambda (função anônima)

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['elefante', 'leão', 'macaco', 'hipopótamo']

print(contador_letras(lista_animais))
lista = ['elefante', 'leão', 'macaco', 'hipopótamo']

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(45, 56))
print(subtracao(87, 46))

# Criando um DICIONÁRIO para calculadora
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))

soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']


print(soma(10, 5))
print(multiplicacao(56, 8))
