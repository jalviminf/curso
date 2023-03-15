from random import randint

numero = randint(1,5)

chute = int(input ('digite seu chute: '))
#if - se isso ou aquilo
if chute == numero:
    print('parabes vc acertou')
#else - se nao
else:
    print('vc errou era o',numero)

print('fim')    