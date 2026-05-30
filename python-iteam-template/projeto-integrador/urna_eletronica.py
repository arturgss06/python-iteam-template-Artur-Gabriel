
# Projeto Integrador — Urna Eletrônica
# Aluno: Artrur Gabriel Santos De Souza 

# ── Escreva sua solução abaixo ──────────────────────────────────────

from cadidatos import Candidato
from relatorio import mostrar_resultado


# Cadastro dos candidatos
candidato1 = Candidato(10, "Ibukun Dididie", "ABC")
candidato2 = Candidato(20, "Thauan", "DEF")
candidato3 = Candidato(30, "Davi", "GHI")

candidatos = [candidato1, candidato2, candidato3]


# Mostrar candidatos
def mostrar_candidatos():
    print("\n===== CANDIDATOS =====")

    for candidato in candidatos:
        print(candidato)


# Sistema de votação
def votar():
    while True:
        try:
            voto = int(input("\nDigite o número do candidato (0 para encerrar): "))

            if voto == 0:
                break

            encontrado = False

            for candidato in candidatos:
                if candidato.numero == voto:
                    candidato.adicionar_voto()
                    encontrado = True
                    print("Voto registrado com sucesso!")

            if not encontrado:
                print("Candidato não encontrado.")

        except ValueError:
            print("Digite apenas números.")


# Programa principal
print("===== URNA ELETRÔNICA =====")

mostrar_candidatos()
votar()
mostrar_resultado(candidatos)
