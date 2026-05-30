# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: Artur Gabriel Santos de Souza
# Data: 29/05/2026

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    produto = {
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade,
        "preco": preco
    }
    inventario.append(produto)


def buscar_por_codigo(inventario, codigo):
    for produto in inventario:
        if produto["codigo"] == codigo:
            return produto

    return None


def listar_abaixo_do_minimo(inventario, minimo):
    produtos_abaixo = []

    for produto in inventario:
        if produto["quantidade"] < minimo:
            produtos_abaixo.append(produto)

    return produtos_abaixo


def valor_total(inventario):
    total = 0

    for produto in inventario:
        total += produto["quantidade"] * produto["preco"]

    return total

inventario = []

adicionar_produto(inventario, "Teclado", 101, 10, 120.50)
adicionar_produto(inventario, "Mouse", 102, 5, 80.00)
adicionar_produto(inventario, "Monitor", 103, 2, 950.00)

print("Inventário:")
for produto in inventario:
    print(produto)

print("\nBusca pelo código 102:")
print(buscar_por_codigo(inventario, 102))

print("\nProdutos abaixo do mínimo (3 unidades):")
print(listar_abaixo_do_minimo(inventario, 3))

print("\nValor total do inventário:")
print(valor_total(inventario))