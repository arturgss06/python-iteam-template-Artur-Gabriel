# Desafio 05 — Gerenciador de Compras
# Aluno: (Artur Gabriel Santos de Souza)
# Data:  (24/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

compras = []

while True:
    produto = input("Digite um produto para adicionar a sua lista (ou digite fim para sair): ")
    if produto.lower() == "fim":
        break
    compras.append(produto)

print("\nLista de compras: ")
for item in compras:
    print("-", item)


print("Total de itens: ", len(compras))