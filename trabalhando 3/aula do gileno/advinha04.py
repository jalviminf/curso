from random import randint
numero = randint(1,10)
tentativas = 5
while tentativas > 0:
    chute = int(input ('digite seu chute: '))
    if chute == numero:
        print('parabes vc acertou')
        break   
    elif chute  < numero:
        print('errou o numero era maior')   
    else:
        print('vc errou era menor')
    tentativas = tentativas - 1    
print('fim')    