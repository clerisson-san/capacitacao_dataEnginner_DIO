#Trabalhando com métodos e funções
#e Classes

class Calculadora:

    #Pode fazer sem o __init__ se não for inicializar nada
    # def __init__(self):
    #     pass

    #função(TEM RETORNO) que realiza uma soma
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

#instancia calculadora
calculadora = Calculadora()

print(calculadora.soma(10,6))
print(calculadora.subtracao(15,6))
print(calculadora.multiplicacao(9,9))
print(calculadora.divisao(45,5))