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

agenda = Agenda()

agenda.nome, agenda.sobrenome, agenda.data, agenda.cpf = entrada()
agenda.armazena()
agenda.exibe_agenda()
