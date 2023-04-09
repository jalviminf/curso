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


'''clientes = [] #Lista de Clientes

for cliente in range(5):
  nome  = input()
  cpf   = input()
  idade = int(input())
  pessoa = {"nome": nome, "cpf": cpf, "idade": idade}
  clientes.append(pessoa)

for indice in range(5): #Se quiser pode usar len(clientes) que será igual a 5
  print("Cliente:", clientes[indice]["nome"], "CPF:", clientes[indice]["cpf"], "Idade:", clientes[indice]["idade"])'''

'''usuarios = []

while True:
  opcao = int(input("O que você deseja? 1) Cadastrar nome, 2) Sair: "))
  if opcao == 1:
    nome = input("Digite o nome: ")
    usuarios.append(nome)
  elif opcao == 2:
    print("Programa finalizado!")
    break'''

'''class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = (input (numero))
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")

    def transferir(self, outra_conta, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar a transferência.")
        else:
            self.saldo -= valor
            outra_conta.saldo += valor
            print(f"Transferência de R${valor:.2f} realizada com sucesso para a conta de {outra_conta.titular}. Novo saldo da conta {self.numero}: R${self.saldo:.2f}")

    def __str__(self):
        return f"Conta {self.numero} - Titular: {self.titular} - Saldo: R${self.saldo:.2f}"

# Criando duas contas
conta1 = Conta(1234, "João Silva", 1000)
conta2 = Conta(5678, "Maria Souza", 500)

# Realizando operações com a conta 1
print(conta1)
conta1.depositar(500)
conta1.sacar(200)
conta1.transferir(conta2, 300)

# Realizando operações com a conta 2
print(conta2)
conta2.depositar(1000)
conta2.sacar(800)
conta2.transferir(conta1, 200)

# Imprimindo informações das contas novamente
print(conta1)
print(conta2)'''


'''import tkinter as tk

class RestauranteApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora do Restaurante")

        # Criação dos widgets
        self.label_estoque_inicial = tk.Label(master, text="Estoque Inicial:")
        self.label_estoque_inicial.pack()

        self.entry_estoque_inicial = tk.Entry(master)
        self.entry_estoque_inicial.pack()

        self.label_compras_mes = tk.Label(master, text="Compras do Mês:")
        self.label_compras_mes.pack()

        self.entry_compras_mes = tk.Entry(master)
        self.entry_compras_mes.pack()

        self.label_estoque_final = tk.Label(master, text="Estoque Final:")
        self.label_estoque_final.pack()

        self.entry_estoque_final = tk.Entry(master)
        self.entry_estoque_final.pack()

        self.label_faturamento_total = tk.Label(master, text="Faturamento Total:")
        self.label_faturamento_total.pack()

        self.entry_faturamento_total = tk.Entry(master)
        self.entry_faturamento_total.pack()

        self.button = tk.Button(master, text="Calcular CMV", command=self.calculate_cmv)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_cmv(self):
        # Lê os valores de entrada e converte para float
        estoque_inicial = float(self.entry_estoque_inicial.get())
        compras_mes = float(self.entry_compras_mes.get())
        estoque_final = float(self.entry_estoque_final.get())
        faturamento_total = float(self.entry_faturamento_total.get())

        # Calcula o CMV
        cmv = (estoque_inicial + compras_mes - estoque_final) / faturamento_total

        # Verifica se o resultado está dentro do intervalo permitido
        if cmv >= 0.3 and cmv <= 0.4:
            mensagem = "O resultado está dentro do intervalo permitido!"
        else:
            mensagem = "O resultado está fora do intervalo permitido!"

        # Exibe o resultado na interface
        self.result_label.config(text=f"O CMV é de: {cmv:.2f}\n{mensagem}")

root = tk.Tk()
restaurante_app = RestauranteApp(root)
root.mainloop()'''


import tkinter as tk

class RestauranteApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora do Restaurante")

        # Criação dos widgets
        self.label_compras_mes = tk.Label(master, text="Compras do Mês:")
        self.label_compras_mes.pack()

        self.entry_compras_mes = tk.Entry(master)
        self.entry_compras_mes.pack()

        self.label_faturamento_total = tk.Label(master, text="Faturamento Total:")
        self.label_faturamento_total.pack()

        self.entry_faturamento_total = tk.Entry(master)
        self.entry_faturamento_total.pack()

        self.button = tk.Button(master, text="Calcular Porcentagem de Compras", command=self.calculate_porcentagem_compras)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_porcentagem_compras(self):
        # Lê os valores de entrada e converte para float
        compras_mes = float(self.entry_compras_mes.get())
        faturamento_total = float(self.entry_faturamento_total.get())

        # Calcula a porcentagem de compras
        porcentagem_compras = (compras_mes / faturamento_total) * 100

        # Verifica se o resultado está dentro do intervalo permitido
        if porcentagem_compras >= 30 and porcentagem_compras <= 40:
            mensagem = "O resultado está dentro do intervalo permitido!"
        else:
            mensagem = "O resultado está fora do intervalo permitido!"

        # Exibe o resultado na interface
        self.result_label.config(text=f"A porcentagem de compras é de: {porcentagem_compras:.2f}%\n{mensagem}")

root = tk.Tk()
restaurante_app = RestauranteApp(root)
root.mainloop()
