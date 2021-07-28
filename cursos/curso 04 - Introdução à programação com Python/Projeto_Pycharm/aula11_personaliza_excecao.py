#Personalizando exceção do

#Criando uma classe de exceção do
class Error(Exception): #Smpre criado
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        notabm1 = int(input('Entre com uma nota de 0 a 10: '))
        if notabm1 >10:
            raise InputError(':::ERRO::: Nota não pode ser > 10')
        elif notabm1 < 0:
            raise InputError(':::ERRO::: Nota não pode ser menor que ZERO')
        print(notabm1)
        break
    except ValueError:
        print(':::ERRO::: Valor inválido. Digite um número')

    except InputError as ex:
        print(ex)