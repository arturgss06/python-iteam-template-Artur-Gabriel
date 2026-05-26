# Desafio 04 — Tabuada Personalizada
# Aluno: (Artur Gabriel Santos de Souza)
# Data:  (24/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

while True:
        numero = int(input("Digite um numero de 1 a 10 para exibir a tabuada ou digite 0 para sair: "))
        if numero == 0:
               int(input("Programa encerrado!"))
               break
        if 1 <= numero <= 10:
                print(f"\nTabuada do {numero}: ")
                for i in range(1, 11):
                        print(f"{numero} x {i} = {numero * i}")
                else:
                        print("Digite um numero entre 1 e 10")

        