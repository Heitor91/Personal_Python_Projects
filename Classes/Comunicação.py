"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Contém uma classe para definir os meios de contato: email e telefone
Histórico de Modificações:
10/04/2022 - Criado
====================================================================================================================="""
from colorama import init, Back, Fore, Style
init(autoreset=True)


class Contato:
    def __init__(self):
        self.__telefone = []
        self.__celular = []
        self.__email = []

    def numero(self, dado):
        def checa_tipo(tel):
            """Função verifica se o dado informado contém apenas numero e se é celular ou fixo pela quantidade de
            dígitos. Retorna True True para celular, True False para fixo e False False para inválido"""
            if len(tel) == 11 and str(tel).isnumeric():
                return True, True
        valid1, valid2 = checa_tipo(dado)
        if valid1 and valid2:
            self.__celular.append('(' + dado[:2] + ')' + dado[2:7] + '-' + dado[7:])
        elif valid1 and not valid2:
            self.__telefone.append('(' + dado[:2] + ')' + dado[2:6] + '-' + dado[6:])
        else:
            print(Back.RED + Fore.BLACK + Style.BRIGHT + 'Formato invalido!!!')
