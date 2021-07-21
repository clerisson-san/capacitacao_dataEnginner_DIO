# Trabalhando com módulos e classes

from aula07_TV import Televisao
from aula07_calc_01 import Calculadora
from aula08_contador_letras import contador_letras, teste

if __name__ == '__main__':

    television = Televisao()

    ##television.power()
    television.aumenta_canal()
    television.aumenta_canal()

    print(television.ligada)

    calc = Calculadora(5,10)

    print(calc.soma())

    lista = ['elefante', 'leão', 'macaco', 'hipopótamo']

    print(contador_letras(lista))

    print(teste())

