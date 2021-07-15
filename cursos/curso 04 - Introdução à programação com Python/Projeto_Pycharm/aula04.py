# # lacos com for the
#
# numero = int(input("Entre com o número: "))
#
# div = 0
#
# for x in range(1, numero+1):
#     resto = numero % x
#     print(numero,x , resto)
#     if resto == 0:
#        div += 1
#
# if div == 2:
#     print("\nnumero {} é primo".format(numero))
# else:
#     print("\nnumero {} NÃO é primo".format(numero))

#


#while
# num = 0
# while num <= 10:
#     print(num)
#     num +=1


notabm1 = int(input("Nota 1º BIM: "))
while notabm1 > 10:
    notabm1 = int(input("Digitou Errado: Digite a Nota 1º BIM: "))

notabm2 = int(input("Nota 2º BIM: "))
while notabm2 > 10:
    notabm2 = int(input("Nota 2º BIM: "))

notabm3 = int(input("Nota 3º BIM: "))
while notabm3 > 10:
    notabm3 = int(input("Nota 3º BIM: "))

notabm4 = int(input("Nota 4º BIM: "))
while notabm4 > 10:
    notabm4 = int(input("Nota 4º BIM: "))

mediaBim = (notabm1+notabm2+notabm3+notabm4)\
           /4

print("\nMédia do Bim: {}".format(mediaBim))
