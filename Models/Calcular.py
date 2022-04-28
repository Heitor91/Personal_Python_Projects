from random import randint


class Calcular:

    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: float = self._gerar_valor
        self.__valor2: float = self._gerar_valor
        self.__operacao: int = randint(1, 3)
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    def __str__(self: object) -> str:
        op: str = ''
        if self.__operacao == 1:
            op = 'Somar'
        elif self.__operacao == 2:
            op = 'Diminuir'
        elif self.__operacao == 3:
            op = 'Somar'
        else:
            op = 'Operaçâo desconhecida'
        return f'Valor 1: {self.__valor1}\nValor 2: {self.__valor1}\nDificuldade: {self.__dificuldade}\nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> float:
        pass

    @property
    def _gerar_resultado(self: object) -> float:
        pass

    @property
    def checar_resultado(self: object, resposta: float) -> bool:
        pass

    def mostrar_operacao(self: object) -> None:
        pass
