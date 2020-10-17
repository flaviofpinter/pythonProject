from Funcionario import Funcionario
from Protocolos import Protocolos
from termcolor import cprint

class Sistema:

    def __init__(self):
        pass

    def iniciarSistema(self):
        print('Iniciando sistema...')
        print('\n-' * 5)

    def chamarProtocolo(self):
        func = Funcionario(input("\033[93m {}\033[00m" .format("Digite o nome: ")),
                           input("\033[93m {}\033[00m" .format("Digite o ra: ")),
                           input("\033[93m {}\033[00m" .format("Digite a senha: ")))
        atv = input("\033[96m {}\033[00m" .format('Deseja ativar o protocolo?: (s / n) '))
        classprot = Protocolos()
        classprot.iniciarProtocolo(atv, func)
