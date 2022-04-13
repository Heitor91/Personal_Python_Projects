"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Variáveis para padronização de estilo visual via terminal
Histórico de Modificações:
11/04/2022 - Criado
====================================================================================================================="""
from colorama import Back, Fore, Style, init
init(autoreset=True)

fonte_entradas = Fore.BLUE + Style.BRIGHT
fonte_confirmacao1 = Back.GREEN + Style.BRIGHT
fonte_confirmacao2 = Fore.GREEN
fonte_invalido = Back.RED + Fore.WHITE + Style.BRIGHT

print(fonte_entradas + 'Entrada')
print(fonte_invalido + 'Invalido!!!')
print(fonte_confirmacao1 + 'Valido')
print(fonte_confirmacao2 + 'valido')
