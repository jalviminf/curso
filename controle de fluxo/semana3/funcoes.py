'''def meu_nome_func():
    meu_nome = input("digite seu nome:")
    print("ola mundo, meu nome é: ", meu_nome)

retorno = meu_nome_func()
print(retorno)'''

#toda funçao retorna algo 

#validaçao
 
'''def meu_nome_func():
    var_controle = False
    meu_nome = input('digite seu nome:')
    if meu_nome == 'jorge':
        var_controle = True
    print('meu nome é:', meu_nome)
    return var_controle

retorno = meu_nome_func()
if retorno:
    print('nome valido')

else:
    print('nome invalido')''' 

#chamada de func

'''def convercao(numero):
    if numero == 1:
        return "I"
numero = int(input('digite o numero: '))

numero_romano = convercao(numero)

print('Numero em romano' , numero_romano)'''

'''def to_roman_numeral(number):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_numeral = ''
    for value, numeral in roman_numerals.items():
        while number >= value:
            roman_numeral += numeral
            number -= value
    return roman_numeral

# Solicita ao usuário que digite um número inteiro
number = int(input("Digite um número inteiro: "))

# Converte o número para um número romano usando a função to_roman_numeral
roman_numeral = to_roman_numeral(number)

# Exibe o número romano correspondente
print(f"O número romano correspondente a {number} é {roman_numeral}")'''


'''def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


numero = int(input("Digite um número inteiro: "))


resultado = par_ou_impar(numero)


print(f"O número {numero} é {resultado}")'''

'''def soma_tres_numeros(a, b, c):
    return a + b + c


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


soma = soma_tres_numeros(num1, num2, num3)

print("A soma dos três números é:", soma)'''


'''def soma(*valores):
    total = 0
    for valor in valores:
        total = total + valor
    print('resultado:', total)
    
soma(4,2,9)'''
##Atividade M1S2

"""total_5_centavos = 35 * 0.05
total_10_centavos = 50 * 0.10
total_25_centavos = 25 * 0.30
total_50_centavos = 50 * 0.15
total_1_real = 19 * 1

total_caixa = (total_5_centavos + total_10_centavos + total_25_centavos + total_50_centavos + total_1_real)

print (total_caixa)"""

#2
'''horas_estimadas = 80
valor_inicial = 1000.00
valor_hora = 20.45
taxa = 0.15

valor_total = (valor_inicial + horas_estimadas * valor_hora)*(1 + taxa )

print(f'{valor_total:.2f}')'''

#3

'''nomes = ['Elysson', 'Giulia', 'Willian', 'Gileno']

for nome in nomes:
    mensagem = f"Olá, {nome}! Seja bem vindo à nave Imperial dos Siths."
    print(mensagem)'''


'''A = int(input())
B = int(input())
C = int(input())
D = int(input())

DIFERENCA = (A * B - C * D)


print("DIFERENCA =", A * B - C * D)'''


"""NUMBER = int(input())
HOURS = int(input())
SALARIO = float(input())

SALARY = SALARIO * HOURS

print("NUMBER = {}".format(NUMBER))
print("SALARY = {:.2f}".format(SALARY))"""

'''import math

while True:
    try:
        R1, X1, Y1, R2, X2, Y2 = map(int, input().split())
        
        distancia = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
        
        if distancia + R2 <= R1:
            print("RICO")
        else:
            print("MORTO")
    except EOFError:
        break'''

'''def par_impar(numero):
    if numero % 2 == 0: #CONDICAO
        return "Par"
    else:
        return "Ímpar"

numero = int(input())
print(par_impar(numero))'''

'''def conte_os_numeros (numero):
    #a primeira linha define a funçao "nome que quiser" aliada a um parametro
    while numero >= 0: #linha while inicia o loop
         # prestar atençao no espaço q nao existe ">=" 
        print(numero)
        numero -= 1 #essa linha esta subritraindo 1

numero = int(input())#essa linha solicita input
    

conte_os_numeros(numero) #essa linha chama a funçao "nome que quisr" e passa a variavel numero'''

'''def soma_3_numeros(a, b, c):
    soma = a + b + c
    return soma

a = int(input())
b = int(input())
c = int(input())

print(soma_3_numeros(a, b, c))'''


'''def soma ():
    soma = 0
    while True:
        entrada = input()
        if entrada == '-1':
            break
        soma += int(entrada)
    return soma

resultado = soma()
print(resultado)'''

'''def positivo_negativo_zero(numero):
  if numero > 0:
    return 'positivo'
  elif numero < 0:
    return 'negativo'
  else:
    return "zero"
  

numero = int(input())
print(positivo_negativo_zero(numero))'''

'''def gorjeta(valor, porcentagem):
    gorjeta = valor * porcentagem / 100
    return gorjeta

valor_conta = float(input())
porcentagem = int(input())
resultado = gorjeta(valor_conta, porcentagem)
print(f"{resultado:.2f}") '''

'''def conta_letras(letra, frase):
  contagem = 0
  for saida in frase:
        if saida == letra:
            count += 1
  return contagem

letra = input()
frase = input()
saida = conta_letras(letra, frase)
print(saida)'''

'''def conta_letras(letra, frase):
    contagem = 0
    for caractere in frase:
        if caractere == letra:
            contagem += 1
    return contagem
letra = input()
frase = input()
saida = conta_letras(letra , frase)
print(saida)'''

'''def verifica_prefixo(palavra1, palavra2):
    return palavra2.startswith(palavra1)

palavra1 = input()
palavra2 = input()
resultado = verifica_prefixo(palavra1, palavra2)
print(resultado)'''

'''alunos = []
while True:
    opcao = int (input('oq vc deseja, usuario? 1-cadastrar ou 2-sair'))
    if opcao == 1:
        nome = input('digite seu none: ')
        aluno = {'nome': nome}
        alunos.append (aluno)
        print(alunos , len (alunos))
    elif opcao == 2:  
        print('programa encerrado')'''

'''class pessoa:
    def __init__(self):
        print('entrou no construtor')

objeto = pessoa()'''


print("Hello World!")


    