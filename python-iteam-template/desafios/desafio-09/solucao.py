# Desafio 09 — Sistema de Frota
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        self.__quilometragem = 0

    def rodar(self, km):
        self.__quilometragem += km

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Quilometragem: {self.__quilometragem} km")


class Caminhao(Veiculo):
    def __init__(self, marca, ano, capacidade_carga):
        super().__init__(marca, ano)
        self.capacidade_carga = capacidade_carga

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Capacidade de carga: {self.capacidade_carga} toneladas")


class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cilindradas: {self.cilindradas} cc")