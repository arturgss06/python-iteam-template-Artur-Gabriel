# Lista 01 — Questão 07: Progressão e Análise
# Aluno: (Artur Gabriel Santos de Souza)
# Data:  (24/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

notas = []

for i in range(10):

   
    while True:
        try:
            nota = float(input(f"Digite a {i + 1}ª nota (0 a 10): "))

            if 0.0 <= nota <= 10.0:
                notas.append(nota)
                break
            else:
                print("Erro: a nota deve estar entre 0 e 10.")

        except ValueError:
            print("Erro: digite um número válido.")


maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)


acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1


if media >= 7.0:
    classificacao = "Aprovado"
elif media >= 5.0:
    classificacao = "Recuperação"
else:
    classificacao = "Reprovado"

print("\nRESULTADOS")
print(f"Maior nota: {maior_nota:.2f}")
print(f"Menor nota: {menor_nota:.2f}")
print(f"Média: {media:.2f}")
print(f"Quantidade acima da média: {acima_media}")
print(f"Classificação: {classificacao}")

# Comentários:
# - O laço for foi utilizado para ler exatamente 10 notas, pois a quantidade
#   de repetições é conhecida antecipadamente.
# - O laço while foi utilizado na validação da entrada porque não sabemos
#   quantas tentativas o usuário fará até informar uma nota válida.
# - Outro for foi utilizado para percorrer a lista de notas e contar quantas
#   ficaram acima da média.