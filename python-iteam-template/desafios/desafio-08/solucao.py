# Desafio 08 — Banco Digital
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor 
        print(f"Depósito de R${valor:.2f} realizado.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente.")

    def exibir_extrato(self):
        print("=== EXTRATO ===")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo:.2f}")