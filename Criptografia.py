import random
import math


class Criptografia:
    # Tabela de código P e Q
    _tabela_primos_ = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                       101,
                       103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                       179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
                       281,
                       283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
                       409,
                       419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523,
                       541,
                       547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
                       659,
                       661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                       809,
                       811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887]

    def __init__(self):
        self.chaves = self._keyGen_()

    # Lista de divisores
    def _div_(self, e):
        divisores = []
        for i in range(1, e + 1):
            if e % i == 0:
                divisores.append(i)
        return divisores

    # Comparação das listas
    def _verificarDiv_(self, div_e, div_t_n):
        listaDivisoresComum = []
        for i in range(0, len(div_e) - 1):
            for k in range(0, len(div_t_n) - 1):
                if div_e[i] == div_t_n[k]:
                    listaDivisoresComum.append(div_e[i])
        return listaDivisoresComum
        
    def _keyGen_(self):
        # Chave Privada 1
        p = random.choice(self._tabela_primos_)
        # Chave Privada 2
        q = random.choice(self._tabela_primos_)
        t_n = (p - 1) * (q - 1)

        # Chaves públicas 1
        n = p * q

        # Chaves públicas 2
        control = True
        while control:
            e = random.randint(1, t_n)
            div_e = self._div_(e)
            div_t_n = self._div_(t_n)
            c = self._verificarDiv_(div_e, div_t_n)
            if len(c) == 1 and c[0] == 1:
                control = False

        # Chave Privada 3
        control = True
        while control:
            d = random.randint(0, 900000)
            mult = d * e
            if mult % t_n == 1:
                control = False

        return n, e, d

    def codificacao(self, msg):
        # Tabela ASCII e Codificação da sentença
        cod = []
        indexList = []
        for i in range(len(msg)):
            indexList.append(ord(msg[i]))
            cod.append((indexList[i] ** self.chaves[1]) % self.chaves[0])

        return cod

    def decodificacao(self, msg):
        lista = msg.split(" ")
        decod = ""
        for i in range(0, len(lista)):
            c = int(lista[i])
            r = (c ** self.chaves[2]) % self.chaves[0]
            decod += chr(r)
        return decod
