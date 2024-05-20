nome_banco = "HBank"

menu = f"""
Bem-vindo ao {nome_banco}, seu banco de toda hora!

Selecione a opção desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Empréstimo
[5] Transferência
[6] Pagamento
[7] Configurações
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
limite_emprestimo = 1000
juros = 0.05  # 5% de juros
numero_parcelas = 12
emprestimos_contratados = []

# Dicionários
clientes = {
    "123456": {"nome": "João", "senha": "senha123", "telefone": "123456789"}
}

fornecedor = {
    "nome": "Fornecedor XYZ",
    "conta": "987654",
    "valor_pagamento": 100  # Valor fixo do pagamento
}

while True:
    opcao = int(input(menu))

# DEPOSITAR
    if opcao == 1:
        valor = float(input("Quanto deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

# SACAR
    elif opcao == 2:
        valor = float(input("Quanto deseja sacar? "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

# EXTRATO
    elif opcao == 3:
        print("\n============ EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        if emprestimos_contratados:
            print("Empréstimos contratados:")
            for emprestimo in emprestimos_contratados:
                print(f"  Valor: R$ {emprestimo['valor']:.2f}, Parcelas: {emprestimo['parcelas']}, Juros: {emprestimo['juros']:.2f}")
        print("=============== FIM ===============")

# EMPRESTIMO
    elif opcao == 4:
        valor = float(input("Qual valor do empréstimo deseja solicitar? "))
        if valor > 0 and valor <= limite_emprestimo:
            parcelas = int(input(f"Em quantas parcelas (máx {numero_parcelas}) deseja pagar? "))
            if 1 <= parcelas <= numero_parcelas:
                valor_total = valor * (1 + juros)
                saldo += valor
                extrato += f"Empréstimo: R$ {valor:.2f}, Total com juros: R$ {valor_total:.2f}\n"
                emprestimos_contratados.append({"valor": valor, "parcelas": parcelas, "juros": valor_total})
                print(f"Empréstimo de R$ {valor:.2f} aprovado! Total a pagar com juros: R$ {valor_total:.2f} em {parcelas} parcelas.")
            else:
                print(f"Operação falhou! O número de parcelas deve ser entre 1 e {numero_parcelas}.")
        else:
            print(f"Operação falhou! O valor do empréstimo deve ser positivo e até R$ {limite_emprestimo:.2f}.")

# TRANSFERENCIA
    elif opcao == 5:
        print("Opção de Transferência selecionada.")
        destino = input("Digite o número da conta de destino: ")
        if destino in clientes:
            valor = float(input("Digite o valor a ser transferido: "))
            if valor > 0 and valor <= saldo:
                saldo -= valor
                extrato += f"Transferência: R$ {valor:.2f} para conta {destino}\n"
                print("Transferência realizada com sucesso!")
            else:
                    print("Transferência falhou! Saldo insuficiente.")
        else:
            print("Transferência falhou! Conta de destino não encontrada.")

# PAGAMENTO
    elif opcao == 6:
        print("Opção de Pagamento selecionada.")
        if saldo >= fornecedor["valor_pagamento"]:
            saldo -= fornecedor["valor_pagamento"]
            extrato += f"Pagamento para {fornecedor['nome']}: R$ {fornecedor['valor_pagamento']:.2f}\n"
            print("Pagamento efetuado com sucesso!")
        else:
            print("Pagamento falhou! Saldo insuficiente.")

# CONFIGURAÇOES
    elif opcao == 7:
        print("Opção de Configurações selecionada.")
        numero_conta = input("Digite o número da sua conta: ")
        senha_atual = input("Digite sua senha atual: ")
        if numero_conta in clientes and clientes[numero_conta]["senha"] == senha_atual:
            nova_senha = input("Digite a nova senha: ")
            clientes[numero_conta]["senha"] = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("Falha ao alterar a senha! Número de conta ou senha incorretos.")

# SAIR
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
