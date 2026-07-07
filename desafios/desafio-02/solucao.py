# Desafio 02 — Calculadora de IMC
# Aluno: (Artur Gabriel Santos de Souza)
# Data:  (24/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"Olá {nome} seu imc é {imc:.2f}")
 