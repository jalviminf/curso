'''print("Hello World!")'''

'''A = int(input())
B = int(input())

print ('X = ', A + B)'''


'''raio = float(input())
n = 3.14159
area = n*raio*raio
print(f"A=",area)'''

#listas []
#tuplas ()
#dicionarios{}

'''nome = "jorge"
for indice in range(5):
   print(nome[indice])'''

'''miha_lista = [2,3,4,5,6,7,8,9]
#indice posiçao
print(miha_lista[4:6])'''

#indices

'''minha_lista= [["emanuel","carlos","rafael"],[9.5,7.5,8.4]]
print(minha_lista[0][1])
print(minha_lista[1][2])'''



'''alunos = [] #armazena os nomes dos alunos
for indice in range (8):
    nome = input('digite seu nome: ')
    alunos.append(nome)
print (alunos)'''    


clientes = [] #Lista de Clientes

for cliente in range(5):
  nome  = input()
  cpf   = input()
  idade = int(input())
  pessoa = {"nome": nome, "cpf": cpf, "idade": idade}
  clientes.append(pessoa)

for indice in range(5): #Se quiser pode usar len(clientes) que será igual a 5
  print("Cliente:", clientes[indice]["nome"], "CPF:", clientes[indice]["cpf"], "Idade:", clientes[indice]["idade"])