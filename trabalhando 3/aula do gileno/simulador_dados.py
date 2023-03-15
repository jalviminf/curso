from random import randint

quantidade = int(input('digite a quantidade de dados'))
tentativa = 1
while tentativa <= quantidade:
    valor=randint(1,6)
    print(valor)
    tentativa = tentativa + 1

print('fim')