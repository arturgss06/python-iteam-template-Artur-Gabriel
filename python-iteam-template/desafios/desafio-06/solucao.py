# Desafio 06 — Bio-Cadastro
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
equipe = []

while True:
    nome = input("Digite o nome do colaborador(ou 'sair' para encerrar): ")

    if nome.lower() == 'sair':
        break

    cargo = input ("Digite o cargo do colaborador: ")


    colaborador = {
        "nome": nome,
        "cargo":cargo
    }

    equipe.append(colaborador)

print("\n--- Lista de Funcionários ---")


for funcionario in equipe:
    print(f"Funcionário: {funcionario['nome']} | Cargo: {funcionario['cargo']}")
    