from Funcionario import Funcionario
from Protocolos import Protocolos


class Sistema:

    def __init__(self):
        pass

    def iniciarSistema(self):
        print('Iniciando sistema...')
        print('\n-' * 10)

    def chamarProtocolo(self):
        func = Funcionario(input("Digite o nome: "), input("Digite o ra: "), input("Digite a senha: "))
        atv = input('Deseja ativar um protocolo?: (s / n) ')
        classprot = Protocolos()
        classprot.iniciarProtocolo(atv, func)
