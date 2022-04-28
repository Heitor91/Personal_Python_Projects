"""class Numeros:

    def __init__(self, tipo):
        self.__tipo = tipo
        self.__lista_de_numeros = []

    def guarda(self, numero):
        self.__lista_de_numeros.append(numero)

    def exibe(self):
        for item in self.__lista_de_numeros:
            print(item)


inteiros = Numeros('Corporativo')
inteiros.guarda(56)
inteiros.exibe()
inteiros.guarda(56)
inteiros.guarda(86)
inteiros.guarda(12)
inteiros.guarda(95)
inteiros.guarda(5)
inteiros.exibe()

class Produto:

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def exibe(self):
        print(f'Nome: {self.__nome} | Valor: {self.__valor}')


class Catalogo(Produto):

    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        # self.__tipo = tipo
        self.__lista_de_produtos = []

    def guarda(self):
        self.__lista_de_produtos.append([self.nome, self.valor])

    def exibe(self):
        print('Produtos:')
        for item in self.__lista_de_produtos:
            print(f'Item: {item[0]}\tValor: {item[1]}')


p1 = ['PlayStation 5', "R$5.000,00"]
lista = Catalogo(p1[0], p1[1])
lista.guarda()
lista.exibe()
p1 = ['Xbox S', "R$5.600,00"]
# lista = Catalogo('Eletrônicos', p1[0], p1[1])
lista.nome, lista.valor = p1[0], p1[1]
lista.guarda()
lista.exibe()

----------------------------------------------------------------------
capture output text in terminal during unittest's

import io
import sys


def foo():
    print("hi")


def test_foo():
    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output  # and redirect stdout.
    foo()  # Call function.
    sys.stdout = sys.__stdout__  # Reset redirect.
    print('Captured', captured_output.getvalue())  # Now works as before.


test_foo()
"""
data = '13/12/1991'
print(data)
print(data.split('/'))
print(data)
data = '13121991'
print(data)
print(data.split())
