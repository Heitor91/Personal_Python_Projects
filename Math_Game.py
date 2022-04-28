"""
Heitor de Carvalho
Projeto 1 do Curso da Geek University (via Udemy)
Obs: O projeto será refatorado en outro programa
==================================================================================================================
Descrição:
Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher o nível de dificuldade do jogo
e após isso gera e apresenta, de forma aletaória, um cálculo para que possamos informar o resultado. Iremos limitar as
operações em somar, diminuir e multiplicar. Se o usuário acertar a resposta, somará 1 ponto ao seu score. Acertando ou
errando, ele poderá ou não continuar o jogo.
"""
from Models.Calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informae o nível de dificuldade desejada [1, 2, 3, 4]'))
    calc: Calcular = Calcular(dificuldade)
    print('Informe o resultado para a seguinte operação:')
    calc.mostrar_operacao()
    resultado: int = int(input())
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s)')    # Outra parte que não faz o menor sentido
    # Trocar essa merda por entrada str S e N responsiva e recursiva recusando entrada inválida
    continuar: int = int(input('Deseja continuar? [1 - sim, 0 - não]: '))
    if continuar:
        jogar(pontos)  # Mudar essa recursividade imbecil
    else:
        print(f'Você finalizou com {pontos} ponto(s)')
        print(f'Até a próxima!')


if __name__ == '__main__':
    main()
