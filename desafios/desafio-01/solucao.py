# Desafio 01 — Seu Primeiro Script
# Aluno: (Artur Gabriel Santos de Souza)
# Data:  (24/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

from datetime import datetime 

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano nascimento: "))

ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento 

print("\n Dados do Usuário ")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos ")