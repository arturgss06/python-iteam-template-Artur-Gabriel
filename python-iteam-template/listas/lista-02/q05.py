# Lista 02 — Questão 05: Funções de Alta Ordem
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q05.py: escreva aplicar(lista, funcao) que retorna uma nova lista com a
# função aplicada a cada elemento. Demonstre com:
#   (a) função que eleva ao quadrado
#   (b) função que retorna True se o número for par
# 
# Em q05_resposta.txt: explique o que significa dizer que funções são
# 'cidadãs de primeira classe' em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def aplicar(lista, funcao):
    nova_lista = []

    for elemento in lista:
        nova_lista.append(funcao(elemento))

    return nova_lista

def quadrado(numero):
    return numero ** 2

def par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5]

print(aplicar(numeros, quadrado))
print(aplicar(numeros, par))
