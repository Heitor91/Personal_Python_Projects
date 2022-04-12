"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Funções compleentares ao código principal
Histórico de Modificações:
11/04/2022 - Criado
====================================================================================================================="""
from colorama import Fore, Back, Style, init
import os
init(autoreset=True)


def entrada():
    def nome():
        while True:
            aux = input(Back.BLUE + Fore.WHITE + Style.BRIGHT + 'Insira o primeiro nome:').capitalize()
            if aux.replace(' ', '').isalpha():
                return aux
            print()

    def sobrenome():
        while True:
            aux = input(Back.BLUE + Fore.WHITE + Style.BRIGHT + 'Insira o primeiro nome:').capitalize()
            if aux.replace(' ', '').isalpha():
                return aux
            print()

    def data():
        pass

    def cpf():
        pass

    return [nome(), sobrenome(), data(), cpf()]
