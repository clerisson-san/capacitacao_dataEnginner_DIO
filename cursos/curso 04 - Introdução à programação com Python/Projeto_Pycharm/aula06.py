#Organizando conjunto e subconjuntos do
#não permite duplicidades

# conjunto = {1,2,3,4,4,2}
#
# #adicionando elementos
# conjunto.add(5)
#
# #removendo elementos
# conjunto.discard(2)
#
# print(type(conjunto))
#
#print(conjunto)

#União de conjuntos
# conjunto = {1,3,5,7,9}
# conjunto2 = {0,2,4,5,6,8,10}
# conjunto_uniao = conjunto.union(conjunto2)
#
#print(conjunto_uniao)

#intersecção de conjuntos
# conjunto_interseccao = conjunto.intersection(conjunto2)
#
# print(conjunto_interseccao)

# #diferença entre conjunto_interseccao
# conjunto_diferenca = conjunto.difference(conjunto2)
# conjunto_diferenca2 = conjunto2.difference(conjunto)
#
# print("Diferença conj. 1 e conj. 2: {}".format(conjunto_diferenca))
# print("Diferença conj. 2 e conj. 1: {}".format(conjunto_diferenca2))

#Diferença SIMETRICA
# conjunto_diff_Simetrica = conjunto.symmetric_difference(conjunto2)
#
# print("Diferença simetrica: {}".format(conjunto_diff_Simetrica))

conjunto_a = {1,3,5,7,9}
conjunto_b = {0,1,2,3,4,5,6,7,8,9,10}

#Subconjuntos
conjunto_subset = conjunto_a.issubset(conjunto_b)
conjunto_subset_2 = conjunto_b.issubset(conjunto_a)

#Superconjunto
print(conjunto_subset_2)
conjunto_superset = conjunto_b.issuperset(conjunto_a)

print("Conj. A é Superconjunot de Conj. B?: {}".format(conjunto_superset))

#Transformando lista em conjuntos
lista_animais = ['cachorro', 'cachorro', 'macaco','gato', 'macaco', 'papagaio', 'periquito']
conjunto_animais = set(lista_animais)
lista_animais = list(conjunto_animais)

print(conjunto_animais)
print(lista_animais)