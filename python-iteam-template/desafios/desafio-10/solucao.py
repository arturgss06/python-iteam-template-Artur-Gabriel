# Desafio 10 — Projeto Final — Urna Eletrônica
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

candidatos = {
    10: {"nome": "Thauan", "partido": "ABC", "votos": 0},
    20: {"nome": "Ibukun Didier", "partido": "DEF", "votos": 0},
    30: {"nome": "Davi", "partido": "GHI", "votos": 0}
}

# Função para mostrar candidatos
def mostrar_candidatos():
    print("\n===== CANDIDATOS =====")
    for numero, dados in candidatos.items():
        print(f"{numero} - {dados['nome']} ({dados['partido']})")


# Função para votar
def votar():
    while True:
        try:
            voto = int(input("\nDigite o número do candidato (0 para encerrar): "))

            if voto == 0:
                break

            if voto in candidatos:
                candidatos[voto]["votos"] += 1
                print("Voto registrado com sucesso!")
            else:
                print("Candidato não encontrado. Tente novamente.")

        except ValueError:
            print("Digite apenas números.")


# Função para mostrar resultado
def resultado():
    print("\n===== RESULTADO FINAL =====")

    maior_voto = 0
    vencedor = ""

    for numero, dados in candidatos.items():
        print(f"{dados['nome']} - {dados['votos']} voto(s)")

        if dados["votos"] > maior_voto:
            maior_voto = dados["votos"]
            vencedor = dados["nome"]

    print(f"\nVencedor da eleição: {vencedor}")



print("URNA ELETRÔNICA ")

mostrar_candidatos()
votar()
resultado()