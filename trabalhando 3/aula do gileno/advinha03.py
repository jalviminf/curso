from random import randint

numero = randint(1,5)

chute = int(input ('digite seu chute: '))
#if - se isso ou aquilo
if chute == numero:
    print('parabes vc acertou')
#elif se nao se    
elif chute  < numero:
    print('errou o numero era maior')   
#else - se nao
else:
    print('vc errou era menor')

print('fim')    