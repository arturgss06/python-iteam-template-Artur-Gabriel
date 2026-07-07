# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: (Artur Gabriel)
# Data:  (22/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
nome = input("seu Nome completo é : ")
cpf = input ("seu CPF é : ")
altura = float(input("sua altura é de : "))

try:
    anonascimento = int(input("ano de nascimento: "))

    idade = 2026 - anonascimento

    print (f"\nNome: {nome}")
    print (f"\nCPF: {cpf}")
    print (f"Ano de Nascimento: {anonascimento}")
    print (f"\nAltura: {altura: .2f} m")
    print (f"Idade em 2026: {idade} anos")

except ValueError:
    print("erro: o ano de nascimento deve ser um número inteiro.")


    