"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Programa responsável por gerar uma agenda coorporativa digital, podendo cadastrar empresas, pessoas podendo vincular
ambos os dados
Histórico de Modificações:
10/04/2022 - Criado
====================================================================================================================="""
# import os
from Auxiliar_Functions.Input_Usuário import entrada
from Classes.Agenda import Agenda
from Classes.Pessoa import Pessoa

agenda = Agenda
pessoa = Pessoa

pessoa.nome, pessoa.sobrenome, pessoa.data, pessoa.cpf = entrada()
agenda.exibe_agenda()
