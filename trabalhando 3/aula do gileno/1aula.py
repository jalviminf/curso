#Variaveis
#Comportamento no algoritmo
#um nome qualquer
# atribuir usa =
#nome = 'jorge' #tipo str

#numero = 42    #tipo inteiro int

#numero_com_virgula = 1199.99 #tipo float

#print(nome) #permitir a visualizacao das informacoes na tela


#Operadores aritimeticos (+ - * / **)
#print(5 + 10)
#print(25 - 9)
#(input)muito util para a interaçao com o usuario

#operadores de comparacao (> < >=  <=  ==  !=)

# = atribuiçao == igualdade

#operadores logicos (AND OR NOT)
# AND - 'E' EM PORTUGUES
#retorna true quando todas as operacoes sao verdade


#print(True and True)

"""ensolarado = True
calor = True
if ensolarado and calor:
    print('eu vou a praia!')
else:
    print('nao vou a praia')"""

#estruturas condicionais (if elif else)


"""if idade >= 18:
    print('é maior de idade!')
else:
    print('nao e mair de idade')"""



"""idade = 1
if (idade >= 18) and (idade < 65):
    print("É Adulto!")
elif (idade < 18) and (idade >= 13):
    print("É Adolescente!")
elif (idade < 13) and (idade > 0):
    print("Criança")
elif (idade >= 65):
    print("É idoso")"""
#revisao 
'''nota1 = float(input('digite a nota: '))
nota2 = float(input('digite a nota: '))
media = (nota1+nota2)/2
print (media)'''


'''nota1 = float(input('digite a nota: '))
nota2 = float(input('digite a nota: '))
media = (nota1+nota2)/2
print(media)
if media >= 7:
    print('aprovado')
else:
  if media < 5:
    print('reprovado')
  else:
     print('recuperacao')'''

'''nota1 = float(input('digite a nota: '))
nota2 = float(input('digite a nota: '))
media = (nota1+nota2)/2
print(media)
if media >= 7:            #primeiro
    print('aprovado')
elif media < 5:
    print('reprovado')
else:                      # ultimo
    print('recuperacao')'''

'''for notas in range (2):
    nota1 = float(input('digite a nota: '))
    nota2 = float(input('digite a nota: '))
    media = (nota1+nota2)/2
    print(media)
    if media >= 7:            #primeiro
        print('aprovado')
    elif media < 5:
        print('reprovado')
    else:                      # ultimo
        print('recuperacao')'''

#listas

'''nomes = ['jorge','lala','jaja','dida']
tamanho = len(nomes)
for i in range(tamanho):
    print(i,nomes[i])'''

'''usuarios = []
while True:
    opcao = int(input('o que vc deseja? 1 ) cadastrar nome , 2 ) sair : '))
    if opcao == 1:
        nome = input('digite o nome: ')
        usuarios.append(nome)
        print(usuarios,len (usuarios))
    elif opcao == 2:
        print('programa finalizado!')
        break

print(usuarios) '''


cliente = {'nome':'jorge','cpf':'32932821806','idade':38}

print(cliente.items())

for chave in cliente:
    print(chave,cliente[chave])
