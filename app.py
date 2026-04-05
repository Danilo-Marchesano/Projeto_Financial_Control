def adicionar_transacao(transacoes):
    # pede o tipo até o usuário digitar certo
    while True:
        tipo = input("Digite 'entrada' ou 'saida': ").lower()
        if tipo in ["entrada", "saida"]:
            break
        else:
            print("Tipo inválido. Tente novamente.")

    # garante que o valor seja número
    while True:
        try:
            valor = float(input("Digite o valor da transação: "))
            break
        except ValueError:
            print("Digite um valor válido.")

    descricao = input("Breve descrição da transação: ")

    # adiciona na lista como dicionário
    transacoes.append({
        "tipo": tipo,
        "valor": valor,
        "descricao": descricao
    })

    print("Transação adicionada com sucesso!")
    print(f"Tipo: {tipo} | Valor: R$ {valor:.2f} | Descrição: {descricao}")


def listar_transacoes(transacoes):
    # verifica se tem algo na lista
    if len(transacoes) == 0:
        print("Nenhuma transação cadastrada.")
    else:
        # percorre e mostra cada transação
        for t in transacoes:
            print(f"Tipo: {t['tipo']} | Valor: R$ {t['valor']:.2f} | Descrição: {t['descricao']}")


def calcular_saldo(transacoes):
    # se não tiver nada, nem tenta calcular
    if len(transacoes) == 0:
        print("Nenhuma transação cadastrada.")
    else:
        saldo = 0

        # soma entradas e subtrai saídas
        for a in transacoes:
            if a["tipo"] == "entrada":
                saldo += a["valor"]
            elif a["tipo"] == "saida":
                saldo -= a["valor"]

        print(f"Saldo atual: R$ {saldo:.2f}")


def ver_resumo(transacoes):
    # mesma ideia: só roda se tiver dados
    if len(transacoes) == 0:
        print("Nenhuma transação cadastrada.")
    else:
        total_entrada = 0
        total_saida = 0

        # separa entradas e saídas
        for a in transacoes:
            if a["tipo"] == "entrada":
                total_entrada += a["valor"]
            elif a["tipo"] == "saida":
                total_saida += a["valor"]
            print(f"Tipo: {a['tipo']} | Valor: R$ {a['valor']:.2f} | Descrição: {a['descricao']}")

        saldo = total_entrada - total_saida

def remover_transacao(transacoes):
    if len(transacoes) == 0:
        print("Nenhuma transação para remover.")
        return

    # mostra a lista com índice
    for i, t in enumerate(transacoes):
        print(f"{i} - {t['tipo']} | R$ {t['valor']:.2f} | {t['descricao']}")

    while True:
        try:
            indice = int(input("Digite o número da transação que deseja remover: "))

            if 0 <= indice < len(transacoes):
                removida = transacoes.pop(indice)
                print("Transação removida com sucesso!")
                print(f"Removida: {removida['tipo']} | R$ {removida['valor']:.2f}")
                break
            else:
                print("Índice inválido.")
        except ValueError:
            print("Digite um número válido.")


def sistema_financeiro():
    # lista principal que guarda tudo
    transacoes = []

    while True:
        print("\n1 - Adicionar transação")
        print("2 - Listar transações")
        print("3 - Ver saldo")
        print("4 - Ver resumo")
        print("5 - Remover transação")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_transacao(transacoes)

        elif opcao == '2':
            listar_transacoes(transacoes)

        elif opcao == '3':
            calcular_saldo(transacoes)

        elif opcao == '4':
            ver_resumo(transacoes)

        elif opcao == '5':
            remover_transacao(transacoes)

        elif opcao == '6':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


# inicia o sistema
sistema_financeiro()