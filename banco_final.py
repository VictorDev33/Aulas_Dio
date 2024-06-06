menu = """
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

"""
saldo = 0
Limite_saque = 500
Saque_maximo = 2
Numero_saques = 0
Extrato = ''


while True:
    opcao = input(menu)
    if opcao == 's':
        valor = float(input('Digite o valor do Saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > Limite_saque
        excedeu_saque = Numero_saques > Saque_maximo 
        if excedeu_saldo:
            print('Saldo insuficiente!')
        elif excedeu_limite:
            print('Excedeu limite! Limite máximo é R$500,00')
        elif excedeu_saque:
            print('Limite de saque diário (3) atingido')
        elif valor >0:
            saldo -= valor
            Numero_saques += 1
            Extrato += f'Saque: RS {valor:.2f}\n'

        else:
            print('Formato inválido, digite um número positivo')
    if opcao == 'd':
        valor = float(input('Digite um valor de depósito: '))
        valor_negativo = valor < 0
        if valor_negativo:
            print('Formato inválido, digite um número positivo')
        else:    
            saldo += valor
            Extrato += f'Depósito: R$ {valor:.2f}\n'
            
        
    
    if opcao == 'e':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    if opcao == 'q':
        break
