# Trabalhando com operadores e formatação

value1 = int(input("Entre com valor 01: "))
value2 = int(input("Entre om o valor 02: "))

sum = value1 + value2
subtract = value1 - value2
multiply = value1 * value2
divide = value1 / value2

result = ('\nSoma: {soma} - '
'\nSubtração: {sub} - '
'\nMultiplicação: {mult} - '
'\nDivisao: {div}'
.format(soma=sum,
        sub=subtract,
        mult=multiply,
        div=int(divide)))

print(result)