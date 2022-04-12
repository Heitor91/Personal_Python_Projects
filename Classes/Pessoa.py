"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Contém uma classe para definir os dados básicos de uma pessoa
Histórico de Modificações:
10/04/2022 - Criado
====================================================================================================================="""
from Classes.Comunicação import Contato


class Pessoa(Contato):
    def __init__(self, nome, sobrenome, data, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__data = data
        self.__cpf = cpf
        super().__init__()

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def data(self):
        return self.__data

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @data.setter
    def data(self, data):
        self.__data = data

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
