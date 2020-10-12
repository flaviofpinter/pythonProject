from Criptografia import Criptografia


class Protocolos:
    def __init__(self):
        pass

    def iniciarProtocolo(self, atv, func):

        if atv == 's':
            print('Iniciando Protocolo Emergêncial')
            print('\n-' * 10)
            if func.eValido():
                print(f'Olá, {func.nome}! seu acesso foi autorizado!')
            else:
                print("Acesso negado!")
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
        print('\n-' * 10)
        print("Iniciando Protocolo de Comunicação")
        print('\n-' * 10)
        cripto = Criptografia()
        msg = input('Digite a mensagem que deseja codificar: ')
        rcod = cripto.codificacao(msg)
        print(*rcod)
        dados = input("Digite a mensagem que quer decodificar: ")
        rdecod = cripto.decodificacao(dados)
        print(rdecod)
