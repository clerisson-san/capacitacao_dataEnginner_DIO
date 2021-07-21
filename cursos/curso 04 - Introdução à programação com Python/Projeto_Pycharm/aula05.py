#Trabalhando com listas e Tuplast


lista = [1,15,3,40,19,5,7]
lista_animal = ['cachorro','lobo','arara', 'gato','elefante']
#nova_lista = lista_animal * 3

tupla = (1,10,12,14)

print(lista[0])
print(tupla[2])

#len()

print(len(tupla))
print(len(lista))

# Convertendo lista em tuple()
tupla_animal = tuple(lista_animal)

print(tupla_animal)
print(type(tupla_animal))

#Convertendo tupla em list() conversão
lista_convert = list(tupla)
print(lista_convert)

#alterando a lista
lista_convert[1] = 15

print(lista_convert)


# #.append /.pop /.remove /.sort /.reverse
#
# lista.sort()
# lista_animal.sort()
#
# print(lista)
# print(lista_animal)
#
# lista.reverse()
# lista_animal.reverse()
#
# print(lista)
# print(lista_animal)

#
# print(nova_lista)
# if 'lobo' in lista_animal:
#     print("{} E na lista".format('gato'))
# else:
#     print("{} Ñ E na lista".format('gato'))
#     lista_animal.append('lobo')
#     print(lista_animal)
#
# if 'lobo' in lista_animal:
#     print("{} E na lista".format('gato'))
# else:
#     print("{} Ñ E na lista".format('gato'))
#     lista_animal.append('lobo')
#     print(lista_animal)
#
# lista_animal.pop(2)
# lista_animal.remove('cachorro')
#
# print(lista_animal)

