class Candidato: 
    def __init__(self, numero, nome, partido): 
        self.numero = numero 
        self.nome = nome 
        self.partido = partido 
        self.votos = 0 

    def adicionar_voto(self): 
        self.votos += 1 

    def __str__(self): 
        return f"{self.numero} - {self.nome} ({self.partido})"