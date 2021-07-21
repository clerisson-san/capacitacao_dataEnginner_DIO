#Trabalhando com métodos e funções
#e Classes

class Calculadora:

    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    #função(TEM RETORNO) que realiza uma soma
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == "__main__":

    # instancia calculadora
    calculadora = Calculadora(10,2)

    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())