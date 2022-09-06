import os
print("Hello, World")

os.system('clear')



class Calculadora():
    def __init__(self):
        op = input('''Qual operação você quer fazer?

        Para somar, digite: +
        Para subtrair, digite: -
        Para dividir, digite: /
        Para multiplicar, digite: x

        ''')

        if op == '+':
            self.Soma()
        elif op == '-':
            self.Menos()
        elif op == "/":
            self.Dividir()
        elif op == "x":
            self.Multiplicar()

    def Soma(self):
        os.system('clear')
        print('Digite um número: ')
        n1 = input('')
        os.system('clear')
        print(f'O primeiro Número digitado é: {n1}')

        os.system('clear')
        print('Digite um segundo número: ')
        n2 = input('')
        os.system('clear')
        print(f'O segundo Número digitado é: {n2}')

        soma = int(n1) + int(n2)
        os.system('clear')
        print(f'''A soma é:

        {n1} + {n2}

        total: {soma}

        ''')

    def Menos(self):
        os.system('clear')
        print('Digite um número: ')
        n1 = input('')
        os.system('clear')
        print(f'O primeiro Número digitado é: {n1}')

        os.system('clear')
        print('Digite um segundo número: ')
        n2 = input('')
        os.system('clear')
        print(f'O segundo Número digitado é: {n2}')

        soma = int(n1) - int(n2)
        os.system('clear')
        print(f'''A subtração é:

        {n1} - {n2}

        total: {soma}

        ''')

    def Dividir(self):
        os.system('clear')
        print('Digite um número: ')
        n1 = input('')
        os.system('clear')
        print(f'O primeiro Número digitado é: {n1}')

        os.system('clear')
        print('Digite um segundo número: ')
        n2 = input('')
        os.system('clear')
        print(f'O segundo Número digitado é: {n2}')

        soma = int(n1) / int(n2)

        os.system('clear')
        print(f'''A divisão é:

        {n1} / {n2}

        total: {soma}

        ''')

    def Multiplicar(self):
        os.system('clear')
        print('Digite um número: ')
        n1 = input('')
        os.system('clear')
        print(f'O primeiro Número digitado é: {n1}')

        os.system('clear')
        print('Digite um segundo número: ')
        n2 = input('')
        os.system('clear')
        print(f'O segundo Número digitado é: {n2}')

        soma = int(n1) * int(n2)

        os.system('clear')
        print(f'''A subtração é:

        {n1} X {n2}

        total: {soma}

        ''')

