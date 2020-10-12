from Criptografia import Criptografia
from Funcionario import Funcionario


class Protocolos:
    def __init__(self):
        pass

    def iniciarProtocolo(self, atv, nome, ra, senha):
        func = Funcionario(nome, ra, senha)
        if atv == 's':
            print('Iniciando Protocolo Emergêncial')
            print('\n-' * 10)
            if (ra == 'N2291H6' and nome == "Nayury" and senha == '1704') or \
                    (ra == "F149JF2" and nome == "Flavio" and senha == "1599") or \
                    (ra == "N571586" and nome == "Robert" and senha == "4524") or \
                    (ra == "F327JB5" and nome == "Michael" and senha == "1234") or \
                    (ra == "F311163" and nome == "Samyra" and senha == "0001"):
                print(f'Olá, {nome}! seu acesso foi autorizado!')
            else:
                print('Acesso negado')
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
        print('\n-' * 10)
        print("Iniciando Protocolo de Comunicação")
        print('\n-' * 10)
        cripto = Criptografia()
        val = cripto.keyGen()
        print(val)
        listCripto = cripto.codificacao(val[0], val[1])
        cripto.criarArquivo(listCripto)

        cripto.decodificacao(val[2], val[1])
