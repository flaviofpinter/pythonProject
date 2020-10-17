from Criptografia import Criptografia
from PIL import Image
from termcolor import cprint


class Protocolos:
    def __init__(self):
        pass

    def iniciarProtocolo(self, atv, func):
        if atv == 's':
            print("\033[96m {}\033[00m".format('Iniciando Protocolo Emergêncial'))
            print('\n-' * 5)
            if func.eValido():
                print(f'Olá, {func.nome}! seu acesso foi autorizado!')
            else:
                print("Acesso negado!")
        else:
            img = Image.open('pepita.jpg_large')
            img.show()
            print("Finalizando então...")
            return
        print(
            'Estamos iniciando o processo. '
            '\n-\nApartir de agora todo e qualquer contato externo e interno'
            ' será restrito a apenas as pessoas autorizadas. \n-\n'
            'O acesso à tripulação, assim como a todo conteúdo tóxico radiativo, será controlado. '
            'Somente inspetores devidamente trajados com roupas especiais poderão adentrar no navio.'
            ' Por razões legislativas o navio deve permanecer a uma distância segura: '
            '50 quilômetros da costa e todo e qualquer '
            'contato deverá ser realizado por meio de helicópteros, '
            'para minimizar e restringir o contato. A área '
            'do entorno num raio de 10 quilômetros está isolada.')
        print('\n-' * 5)
        print("\033[96m {}\033[00m".format("Iniciando Protocolo de Comunicação"))
        print('\n-' * 5)
        cripto = Criptografia()

        parar = 0
        while parar == 0:
            pergunta = input("\033[93m {}\033[00m".format("Deseja codificar ou decodificar?(c / d): "))
            val = cripto.keyGen()
            if pergunta == 'c':
                msg = input("\033[93m {}\033[00m".format('Digite a mensagem que deseja codificar: '))
                rcod = cripto.codificacao(msg)
                self._criarArquivo_(rcod)
                cprint(' '.join(map(str, rcod)), 'magenta')
                print("N: ", val[0], "D: ", val[2])
                print("Salve essas duas chaves para decodificações futuras")
            elif pergunta == 'd':
                pgt = input("Gostaria de inserir as chaves D e N ?(s / n): ")
                if pgt == 's':
                    chave_d = int(input("Digite a chave D: "))
                    chave_n = int(input("Digite a chave N: "))
                    cripto.decodificacaoChaves(chave_d, chave_n)
                dados = input("\033[93m {}\033[00m".format("Digite a mensagem que quer decodificar: "))
                rdecod = cripto.decodificacao()
                cprint(rdecod, 'magenta')
            else:
                print("Digite um função válida.")
                continue
            try:
                parar = int(input("\033[93m {}\033[00m".format("Digite 1 para parar o programa.(1 / 0): ")))
            except ValueError:
                print("Opção inválida")

    def _criarArquivo_(self, cod):
        strList = '\n'.join(str(x) for x in cod)
        for f in range(len(cod)):
            f = open("texto_criptografado.txt", "w")
            f.write(f"{strList} ")
            f.close()
