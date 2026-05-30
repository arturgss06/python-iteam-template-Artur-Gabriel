# Desafio 07 — Bio-Calculadora
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
from funcoes_mat import area_circulo, volume_esfera, hipotenusa

print(" BIO CALCULADORA ")
print("1 - Àrea do circulo ")
print("2 - Volume da esfera")
print("3 - Hipotenusa")

opcao = input("Esolha uma opcão: ")

if opcao == "1":
    raio = float(input("Digite o raio: "))
    resultado = area_circulo(raio)
    print(f"Àrea do circulo: {resultado:.2f}")

elif opcao == "2":
    raio = float(input("Digite o raio: "))
    resultado = volume_esfera(raio)
    print(f"Volume da esfera: {resultado:.2f}")

elif opcao == "3":
    cateto1 = float(input("Digite o primeiro cateto: "))
    cateto2 = float(input("Digite o segundo cateto: "))
    resultado = hipotenusa(cateto1, cateto2)
    print(f"Hipotenusa: {resultado:.2f}")

else: 
    print("Opção inválid.")