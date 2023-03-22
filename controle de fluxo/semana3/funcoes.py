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

def soma_tres_numeros(a, b, c):
    return a + b + c


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


soma = soma_tres_numeros(num1, num2, num3)

print("A soma dos três números é:", soma)