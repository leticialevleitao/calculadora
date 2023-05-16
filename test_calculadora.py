from os import name
import pytest

# dupla Júlia Boto e Letícia de Albuquerque
class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise DivError("DivError: divisão por zero")
        resultado = a / b
        if not self.verificar_natural(resultado):
            raise ResultError("ResultError: resultado não é um número natural")
        return resultado

    def verificar_natural(self, num):
        if not isinstance(num, int) or num < 0:
            raise NotNaturalError("NotNaturalError: não é um número natural")
        return True

class DivError(Exception):
    pass

class ResultError(Exception):
    pass

class NotNaturalError(Exception):
    pass

def test_soma():
    calc = Calculadora()
    assert calc.soma(2, 3) == 5
    assert calc.soma(0, 0) == 0
    assert calc.soma(5, 0) == 5
    assert calc.soma(0, 5) == 5

def test_subtracao():
    calc = Calculadora()
    assert calc.subtracao(5, 2) == 3
    assert calc.subtracao(0, 0) == 0
    assert calc.subtracao(5, 0) == 5
    assert calc.subtracao(0, 5) == 5

def test_multiplicacao():
    calc = Calculadora()
    assert calc.multiplicacao(2, 3) == 6
    assert calc.multiplicacao(0, 5) == 0
    assert calc.multiplicacao(5, 0) == 0
    assert calc.multiplicacao(0, 0) == 0

def test_divisao():
    calc = Calculadora()
    assert calc.divisao(6, 2) == 3
    assert calc.divisao(10, 5) == 2
    assert calc.divisao(0, 5) == 0
    with pytest.raises(DivError):
        calc.divisao(5, 0)
    with pytest.raises(ResultError):
        calc.divisao(5, 2)

def test_operadores_naturais():
    calc = Calculadora()
    assert calc.verificar_natural(5)
    assert not calc.verificar_natural(-2)
    assert not calc.verificar_natural(2.5)
    with pytest.raises(NotNaturalError):
        calc.verificar_natural("7")

def test_calculos():
    calc = Calculadora()
    numeros = [(2, 3), (5, 0), (10, 5), (6, 2), (5, 2)]
    operadores = ['+', '-', '*', '/', '/']
    resultados = [5, 5, 2, 3, 2.5]

    for i in range(len(numeros)):
        resultado = calc.calcular(numeros[i], operadores[i])
        assert resultado == resultados[i]

def test_divisao_por_zero():
    calc = Calculadora()
    with pytest.raises(DivError):
        calc.calcular((5, 0), '/')

def test_resultado_nao_natural():
    calc = Calculadora()
    with pytest.raises(ResultError):
        calc.calcular((5, 2), '/')

    if name == 'main':
        pytest.main()
