"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Funções compleentares ao código principal
Histórico de Modificações:
11/04/2022 - Criado
13/04/2022 - Finalizada as 4 funções de entrada
           - Adicionados comentários aos código
====================================================================================================================="""
import datetime
# from colorama import init
from Auxiliar_Functions.Colorama_Styles import fonte_entradas, fonte_invalido
# import os


def entrada():
    """Função responsável pela entrada dos 4 valores a serem inseridos na classe Pessoa. Ele retorna uma lista dos
    retornos das 4 funções dedicadas a cada item"""
    def nome(select=True):
        """Função resposável pela entrada do nome e sobrenome com uma variável booleana para selecionar o dado a ser
        inserido: True(Padrão) -> Nome, False -> sobrenome"""
        while True:
            aux = input(fonte_entradas + f'Insira o {"primeiro" if select else "segundo"} nome:').capitalize()
            if aux.replace(' ', '').isalpha():
                return aux
            print(fonte_invalido + "Inserção de dados inválida")

    def sobrenome():
        """Função chama entrada pela função nome enviando um booleano False para indicar entrada de outro dado. Existe
         uma correção para preposições de sobrenome como 'de' e 'do' por exemplo"""
        while True:
            aux = nome(False).split()
            aux = ' '.join([item if len(item) > 2 else item.lower for item in aux])
            if aux.replace(' ', '').isalpha():
                return aux
            print(fonte_invalido + "Inserção de dados inválida")

    def nascimento():
        """Entrada do dado de data de nascimento e retorna um valor configurado em datetime"""
        def valida_data(ldata):
            """Função que valida os valores da data (ano, mês, dia)
                    - Ano: Deve ser maior que 0 e inferior ao ano corrente
                    - Mês: Deve estar compreendido de 1 a 12 com estes inclusos
                    - Dia: Deve ser positivo e maior que 0, Menor e igual a 31 para os meses mais longos
                           Ser menor que 31 para os meses mais curtos
                           Ser menor ou igual a 29 para o mês 2 em ano bissexto e menor que 29 em ano não bissexto"""
            if 0 <= ldata[2] <= datetime.datetime.year:
                bissexto = True if ldata % 400 else True if ldata % 4 == 0 and ldata % 100 != 0 else False
                mes_curto = True if ldata[1] in [2, 4, 6, 9, 11] else False
                if 1 <= ldata[1] <= 12 and 1 <= ldata[0] <= 31:
                    if mes_curto and ldata[0] < 31:
                        if ldata[1] == 2:
                            return True if ldata[0] < 30 and bissexto else True if ldata[0] < 29 else False
                        return True
                    return False if mes_curto else True
                return False
            return False
        while True:
            data = (input(fonte_entradas + 'Data de nascimento (dd/mm/aaaa):')).split('/')
            data = [int(item) if str(item).isnumeric() else False for item in data]
            if False in data:
                print(fonte_invalido + 'Formato de data inválido')
            else:
                valida_data(data)
                return datetime.datetime(data[2], data[1], data[0])

    def cpf():
        """Função recebe dado do documento de pessoa física e analisa as casas individualmente totalizando 4 casas,
        sendo que é necessário quantidade de digitos em cada casa respectivamente: 3, 3, 3, 1. E validando se deu
        entrada apenas em caracteres numéricos"""
        def valida(aux):
            aux = [aux.split('.')[0], aux.split('.')[1], aux.split('.')[2].split('-')[0], aux.split('-')[1]]
            if len(aux) == 4:
                for item in aux:
                    dig, tam = True if aux.index(item) == 3 else False, len(item)
                    aux[aux.index(item)] = True if dig and tam == 1 else True if tam == 3 else False
                return False if False in aux else True
        while True:
            registro = input(fonte_entradas + 'CPF (000.000.000-0): ')
            if valida(registro):
                return registro
            print(fonte_invalido + "Formato invalido!!!!")
    return [nome(), sobrenome(), nascimento(), cpf()]
