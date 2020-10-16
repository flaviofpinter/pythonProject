class Funcionario:
    company = "F.I.T.A."

    def __init__(self, nome, ra, senha):
        self.nome = nome
        self.ra = ra
        self.senha = senha

    def description(self):
        return f"My name is {self.nome}"

    def eValido(self):
        if (self.ra == 'N2291H6' and self.nome == "Nayury" and self.senha == '1704') or \
                (self.ra == "F149JF2" and self.nome == "Flavio" and self.senha == "1599") or \
                (self.ra == "N571586" and self.nome == "Robert" and self.senha == "4524") or \
                (self.ra == "F327JB5" and self.nome == "Michael" and self.senha == "1234") or \
                (self.ra == "1" and self.nome == "1" and self.senha == "1") or \
                (self.ra == "F311163" and self.nome == "Samyra" and self.senha == "0001"):
            return True
        else:
            return False
