from random import randint
numero = randint(1,100)
tentativas = 5
while tentativas > 0:
    chute = int(input ('digite seu chute: '))
    diferenca = numero - chute
    if chute == numero:
        print('parabes vc acertou')
        break   
    elif diferenca <5 and diferenca >= -5:
        print('errou mas esta perto')
    elif diferenca >0:
        print('vc errou era maior')       
    else:
        print('vc errou era menor')
    tentativas = tentativas - 1    
print('fim')    