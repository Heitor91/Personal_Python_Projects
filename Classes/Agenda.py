"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Contém uma classe para armazenar os dados
Histórico de Modificações:
10/04/2022 - Criado
====================================================================================================================="""
from Classes.Pessoa import Pessoa


class Agenda(Pessoa):
    def __init__(self, nome=None, sobrenome=None, data=None, cpf=None):
        super().__init__(nome, sobrenome, data, cpf)
        self.__agenda = []

    @property
    def agenda(self):
        return self.__agenda

    def armazena(self):
        novo_contato = {'Nome': self.nome, 'Sobrenome': self.sobrenome, 'Nascimento': self.data, 'CPF': self.cpf}
        self.__agenda.append(novo_contato)

    def retorna_index(self, dado):
        for item in self.__agenda:
            if dado == item.get('Nome'):
                return self.__agenda.index(item)
        return None

    def apaga_contato(self, dado):
        self.__agenda.pop(Agenda.retorna_index(self, dado))

    def exibe_agenda(self):
        def imprime(**kwargs):
            for chave in kwargs:
                print(f'{chave}: {kwargs.get(chave)}')
        for contato in self.__agenda:
            imprime(**contato)
