#######################################
# #if / elif / else:
################################
#
# valor01 = int(input("Valor 01: "))
# valor02 = int(input("Valor 02: "))
# valor03 = int(input("Valor 03: "))
#
# if valor01 > valor02 and valor01 > valor03:
#     print("O maior valor é {}".format(valor01))
# elif valor02 > valor01 and valor02 > valor03:
#     print("O maior valor é {}".format(valor02))
# else:
#     print("O maior valor é {}".format(valor03))
# print("Fim do programa")

#################################
#mod / == / or /not
#################################
# entrada_1 = int(input("Entre com o valor 01: "))
# entrada_2 = int(input("Entre com o valor 02: "))
#
# resto_1 = entrada_1 % 2
# resto_2 = entrada_2 % 2
#
# if resto_1 == 0 or not resto_2 > 0:
#     print("Valor 01 digitado: {}".format(entrada_1))
#     print("Valor 02 digitado: {}".format(entrada_2))
#     print("Foi digitado pelo menos um número PAR")
# else:
#     print("Valor digitado 02: {}".format(entrada_2))
#     print("Todos os números digitados são IMPARES")
#
#
#

# <= / =>

notabm1 = int(input("Nota 1º BIM: "))
notabm2 = int(input("Nota 2º BIM: "))
notabm3 = int(input("Nota 3º BIM: "))
notabm4 = int(input("Nota 4º BIM: "))

mediaBim = (notabm1+notabm2+notabm3+notabm4)\
           /4

if notabm1 <= 10 and notabm2 <= 10 and notabm3 <= 10 and notabm4 <= 10:
    print("\nMédia do Bim: {}".format(mediaBim))
else:
    print("\nValor digitado deve ser menor que 10")
