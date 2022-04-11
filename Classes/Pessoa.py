"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Contém uma classe para definir os dados básicos de uma pessoa
Histórico de Modificações:
10/04/2022 - Criado
====================================================================================================================="""


class Pessoa:
    def __init__(self, nome, sobrenome, data, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__data = data
        self.__cpf = cpf
