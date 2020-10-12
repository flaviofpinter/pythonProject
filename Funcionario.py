class Funcionario:
    company = "F.I.T.A."

    def __init__(self, nome, ra, senha):
        self.nome = nome
        self.ra = ra
        self.senha = senha

    def description(self):
        return f"My name is {self.nome}"
