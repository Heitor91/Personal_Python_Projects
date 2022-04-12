"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Funções compleentares ao código principal
Histórico de Modificações:
11/04/2022 - Criado
====================================================================================================================="""
from colorama import init
from Auxiliar_Functions.Colorama_Styles import fonte_entradas, fonte_invalido
import os


def entrada():
    def nome(select=True):
        while True:
            aux = input(fonte_entradas + f'Insira o {"primeiro" if select else "segundo"} nome:').capitalize()
            if aux.replace(' ', '').isalpha():
                return aux
            print(fonte_invalido + "Inserção de dados inválida")

    def sobrenome():
        while True:
            aux = nome(False).split()
            aux = ' '.join([item if len(item) > 2 else item.lower for item in aux])
            if aux.replace(' ', '').isalpha():
                return aux
            print(fonte_invalido + "Inserção de dados inválida")

    def data():
        pass

    def cpf():
        pass

    return [nome(), sobrenome(), data(), cpf()]
