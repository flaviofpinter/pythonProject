from Funcionario import Funcionario
from Protocolos import Protocolos


class Sistema:

    def __init__(self):
        pass

    def iniciarSistema(self):
        print('Iniciando sistema...')
        print('\n-' * 10)

    def chamarProtocolo(self):
        employee = Funcionario(input("Digite o nome: "), input("Digite o ra: "), input("Digite a senha: "))
        atv = input('Deseja ativar um protocolo?: (s / n) ')
        classprot = Protocolos()
        if atv == 's':
            classprot.iniciarProtocolo(atv, employee.nome, employee.ra, employee.senha)
