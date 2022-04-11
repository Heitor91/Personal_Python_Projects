"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Contém uma classe para definir os dados de endereçamento
Histórico de Modificações:
10/04/2022 - Criado
====================================================================================================================="""


class Endereco:
    def __init__(self, logradouro, endereco, cidade, estado, cep):
        self.__logradouro = logradouro
        self.__endereco = endereco
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep