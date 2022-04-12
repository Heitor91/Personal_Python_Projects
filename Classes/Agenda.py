"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Contém uma classe para armazenar os dados
Histórico de Modificações:
10/04/2022 - Criado
====================================================================================================================="""


class Agenda:
    def __init__(self):
        self.__agenda = []

    def armazena(self, dados):
        self.__agenda.append(dados)

    def retorna_index(self, dado):
        return self.__agenda.index(dado)

    def apaga_contato(self, dado):
        self.__agenda.pop(Agenda.retorna_index(self, dado))

    def exibe_agenda(self):
        print(f'{self.__agenda[index]}\n' for index in range(len(self.__agenda)))
