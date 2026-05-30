# Lista 02 — Questão 08: Herança e Polimorfismo
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente:
#   - Funcionario(nome, salario): calcular_bonus() → 10% do salário
#   - Gerente(departamento): bônus = 20%
#   - Estagiario(curso): bônus = 5%
# Crie lista com objetos dos 3 tipos, itere exibindo nome e bônus.
# Explique em comentário: por que o Python chama a versão correta de
# calcular_bonus() sem você verificar o tipo do objeto?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
# Lista 02 — Questão 08: Herança e Polimorfismo
# Aluno: Thauan dos Santos Machado
# Data: 29/05/2026

# ── Sua solução abaixo ──────────────────────────────────────────────────────

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return self.salario * 0.20


class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def calcular_bonus(self):
        return self.salario * 0.05


funcionarios = [
    Funcionario("Carlos", 3000),
    Gerente("Ana", 8000, "TI"),
    Estagiario("Lucas", 1500, "Computação")
]

for funcionario in funcionarios:
    print(f"Nome: {funcionario.nome}")
    print(f"Bônus: R$ {funcionario.calcular_bonus():.2f}")
    print("-" * 30)

    
# O Python chama automaticamente a versão correta do método
# calcular_bonus() por causa do polimorfismo.
# Isso acontece porque cada objeto sabe qual classe pertence,
# então o método correspondente é executado sem precisar verificar
# manualmente o tipo do objeto.