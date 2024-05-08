mensagem = ""

menu = f"""
Você está no XYZ

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(f"{menu}{mensagem}\n=> ")

    mensagem = ""
    if opcao == "d":
        valor = float(input("Qual o valor do seu depósito? "))

        if valor > 0:
            saldo += valor
            extrato += f"+ R$ {valor:.2f}\n"
            mensagem = f"Depósito realizado com sucesso. Saldo: R$ {saldo:.2f}"

        else:
            # print("Por favor, informe um valor maior que 0.")
            mensagem = "Por favor, informe um valor maior que 0."

    elif opcao == "s":
        valor = float(input("Quando você deseja sacar? "))

        if valor > saldo:
            mensagem = "Você não tem saldo suficiente para fazer esse saque. Por favor, verifique se você tem saldo."

        elif valor > limite:
            mensagem = ("Não foi possível fazer o saque pois o valor excede o limite da transação. Por favor, "
                        "escolha outro valor.")

        elif numero_saques >= LIMITE_SAQUES:
            mensagem = "Você excedeu a quantidade diária de saques permitida. Por favor, tente novamente amanhã."

        elif valor > 0:
            saldo -= valor
            extrato += f"- R$ {valor:.2f}\n"
            numero_saques += 1
            mensagem = f"Saque realizado com sucesso. Saldo: R$ {saldo:.2f}"

        else:
            mensagem = "Por favor, informe um valor maior que 0."

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        mensagem_extrato = f"Veja abaixo as suas movimentações:\n\n{extrato}"
        print("Sem movimentações até o momento." if not extrato else mensagem_extrato)
        print(f"Você possui R$ {saldo:.2f} de saldo em sua conta.")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        mensagem = "Operação não reconhecida. Por favor selecione uma das opções acima."
