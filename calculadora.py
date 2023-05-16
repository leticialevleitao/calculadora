import pytest
import os
os.system('cls')

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

def main():
    calc = Calculadora()
    a = int(input("Digite o primeiro número: "))
    b = int(input("\nDigite o segundo número: "))

    print("\nEscolha uma operação:")
    print("\n1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    opcao = int(input("\nOpção: "))

    if opcao == 1:
        resultado = calc.soma(a, b)
        print("\nResultado:", resultado)
    elif opcao == 2:
        resultado = calc.subtracao(a, b)
        print("\nResultado:", resultado)
    elif opcao == 3:
        resultado = calc.multiplicacao(a, b)
        print("\nResultado:", resultado)
    elif opcao == 4:
        try:
            resultado = calc.divisao(a, b)
            print("\nResultado:", resultado)
        except DivError as e:
            print(str(e))
        except ResultError as e:
            print(str(e))
    else:
        print("Opção inválida.")

if __name__ == '__main__':
    main()
