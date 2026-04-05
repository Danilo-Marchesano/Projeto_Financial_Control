import csv

def ler_dados(arquivo):
    vendas = []

    with open(arquivo, mode='r', encoding='utf-8') as file:
        leitor = csv.DictReader(file)

        for linha in leitor:
            linha["quantidade"] = int(linha["quantidade"])
            linha["valor_unitario"] = float(linha["valor_unitario"])
            vendas.append(linha)

    return vendas


def calcular_relatorio(vendas):
    total_geral = 0
    produtos = {}

    for v in vendas:
        total = v["quantidade"] * v["valor_unitario"]
        total_geral += total

        nome = v["produto"]

        if nome in produtos:
            produtos[nome] += total
        else:
            produtos[nome] = total

    return total_geral, produtos


def salvar_relatorio(total_geral, produtos):
    with open("relatorio.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Produto", "Total Vendido"])

        for produto, total in produtos.items():
            writer.writerow([produto, round(total, 2)])

        writer.writerow([])
        writer.writerow(["TOTAL GERAL", round(total_geral, 2)])


def main():
    vendas = ler_dados("vendas.csv")

    total_geral, produtos = calcular_relatorio(vendas)

    salvar_relatorio(total_geral, produtos)

    print("Relatório gerado com sucesso!")


main()