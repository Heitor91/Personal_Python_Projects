"""=====================================================================================================================
Criado por Heitor de Carvalho-------------------------10/04/2022
Arquivo Unittest - Unidades testadas:
- Input_Usuário.py
Histórico de Modificações:
23/04/2022 - Criado
====================================================================================================================="""
import datetime
import io
import sys
import unittest
from unittest.mock import patch
from Auxiliar_Functions.Input_Usuário import nome, sobrenome, nascimento, cpf


class MyTestCase(unittest.TestCase):

    # =================================================================================================================
    # Sequência de testes para a função nome()
    @patch('builtins.input', lambda _: 'Heitor')
    def test_name_pass1(self):
        retorno = nome(teste=True)
        self.assertEqual(retorno, 'Heitor')

    @patch('builtins.input', lambda _: 'heitor')
    def test_name_pass2(self):
        retorno = nome(teste=True)
        self.assertEqual(retorno, 'Heitor')

    @patch('builtins.input', lambda _: 'júlio césar')
    def test_name_pass3(self):
        retorno = nome(teste=True)
        self.assertEqual(retorno, 'Júlio César')

    @patch('builtins.input', lambda _: 'H31T02')
    def test_name_error1(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        nome(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mInserção de dados inválida\n')

    @patch('builtins.input', lambda _: 'H&it0r')
    def test_name_error2(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        nome(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mInserção de dados inválida\n')

    # =================================================================================================================
    # Sequência de testes para a função sobrenome()
    @patch('builtins.input', lambda _: 'silva')
    def test_secname_pass1(self):
        retorno = sobrenome(teste=True)
        self.assertEqual(retorno, 'Silva')

    @patch('builtins.input', lambda _: 'DA silva NAscimento')
    def test_secname_pass2(self):
        retorno = sobrenome(teste=True)
        self.assertEqual(retorno, 'da Silva Nascimento')

    @patch('builtins.input', lambda _: 'D4 S1lvA Nascimento')
    def test_secname_error1(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        nome(select=False, teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mInserção de dados inválida\n')

    @patch('builtins.input', lambda _: 'da Silv@ Nascim&nt0')
    def test_secname_error2(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        nome(select=False, teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mInserção de dados inválida\n')

    # =================================================================================================================
    # Sequência de testes para a função nascimento()
    @patch('builtins.input', lambda _: '13/12/1991')
    def test_birth_pass1(self):
        retorno = nascimento(teste=True)
        self.assertEqual(retorno, datetime.datetime(year=1991, month=12, day=13))

    @patch('builtins.input', lambda _: '13121991')
    def test_birth_error1(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        nascimento(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mFormato de data inválido\n')

    @patch('builtins.input', lambda _: '13-12-1991')
    def test_birth_error2(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        nascimento(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mFormato de data inválido\n')

    @patch('builtins.input', lambda _: '13/21/1991')
    def test_birth_error3(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        nascimento(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mFormato de data inválido\n')

    @patch('builtins.input', lambda _: '13/12/2100')
    def test_birth_error4(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        nascimento(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mFormato de data inválido\n')

    @patch('builtins.input', lambda _: '29/02/2022')
    def test_birth_error5(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        nascimento(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mFormato de data inválido\n')

    # =================================================================================================================
    # Sequência de testes para a função cpf()
    @patch('builtins.input', lambda _: '000.000.000-00')
    def test_cpf_pass1(self):
        retorno = cpf(teste=True)
        self.assertEqual(retorno, '000.000.000-00')

    @patch('builtins.input', lambda _: '00000000000')
    def test_cpf_error1(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        cpf(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mFormato invalido!!!!\n')

    @patch('builtins.input', lambda _: '000.000.000-0')
    def test_cpf_error2(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        cpf(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mFormato invalido!!!!\n')

    @patch('builtins.input', lambda _: '00.000.000-00')
    def test_cpf_error3(self):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        cpf(teste=True)  # Call function
        sys.stdout = sys.__stdout__  # Reset redirect
        self.assertEqual(captured_output.getvalue(), '\x1b[41m\x1b[37m\x1b[1mFormato invalido!!!!\n')


if __name__ == '__main__':
    unittest.main()
