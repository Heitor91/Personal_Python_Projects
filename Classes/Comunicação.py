"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Contém uma classe para definir os meios de contato: email e telefone
Histórico de Modificações:
10/04/2022 - Criado
====================================================================================================================="""
from Auxiliar_Functions.Colorama_Styles import fonte_invalido, fonte_entradas, init, fonte_confirmacao1, \
    fonte_confirmacao2

init(autoreset=True)


class Contato:
    def __init__(self):
        self.__telefone = []
        self.__celular = []
        self.__email = []

    def input_contato(self):
        """Função para entrada do valor do telefone e/ou e-mail em string
            Entrada responsiva ao usuário, programa identifica se é um numeto de telefone ou um email"""

        def email(endereco):
            aux = endereco.split('@')
            aux[0] = aux[0].replace('.', '').replace('_', '').isalpha()
            aux.extend(aux[1].split('.')), aux.pop(1)
            if len(aux) not in [3, 4]:
                return False
            # aux = [prefixo, provedor, 'com', pais*] *se houver
            aux[1] = aux[1].isalpha()
            aux[2] = aux[2] == 'com'
            if len(aux) == 4:
                aux[3] = len(aux[3]) == 2
            return False if False in aux else True

        def telefone(numero):
            return '(' + numero[:2] + ')' + numero[2:7] + '-' + numero[7:]

        def celular(numero):
            return '(' + numero[:2] + ')' + numero[2:6] + '-' + numero[6:]

        while True:
            contato = input(fonte_entradas + "Digite o email (completo), telefone (apenas numeros) ou sair:")
            if contato.isnumeric() and len(contato) == 10:
                self.__telefone.append(telefone(contato))
            elif contato.isnumeric() and len(contato) == 11:
                self.__celular.append(celular(contato))
            elif '@' in contato and email(contato):
                self.__email.append(contato.lower())

            elif contato.lower() == 'sair':
                print(fonte_confirmacao1 + f'Inseridos:')
                print(fonte_confirmacao2 + f'{len(self.__celular)} nº de celular')
                print(fonte_confirmacao2 + f'{len(self.__telefone)} nº de telefone')
                print(fonte_confirmacao2 + f'{len(self.__email)} email(s)')
                return
            else:
                print(fonte_invalido + "Dado em formato inválido, tente novamente")
