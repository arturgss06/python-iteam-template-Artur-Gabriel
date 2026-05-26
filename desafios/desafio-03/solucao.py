# Desafio 03 — Sistema de Multas
# Aluno: (Artur Gabriel Santos de Souza)
# Data:  (24/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
velocidade = float(input("Qual é a velocidade do carro: "))

limite = 80
preco_por_km = 7.00

if velocidade > limite:
    print("Multado! Você excedeu o limite de 80km/h")

    km_excedidos = velocidade - limite 
    valor_multa = km_excedidos * preco_por_km
    print(f"Valor da multa: R$ {valor_multa:.2f}")

elif velocidade  == limite:
    print("Atenção !!! Você está exatamente no limite de 80km/h, cuidado para não acelerar mais")

else:
    print("Boa viagem, vá com segurança !!!!")