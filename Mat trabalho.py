import math
import matplotlib.pyplot as plt
import numpy as np


def menu():
    print(20 * '=', 'Calculadora RMC', 20 * '=')
    print('\n''1. Funções do segundo grau '
          '\n2. Funções exponenciais '
          '\n3. Matrizes '
          '\n4. Sair')
    try:
        resp = int(input('\nO que vc deseja calcular? '))
        if resp == 'Sair' or resp == 'sair':
            print('Thau Thau')
        elif resp == 1:
            print('\nFunções do segundo grau\n')
            funcoes()
        elif resp == 2:
            print('\nFunções exponenciais\n')
            funcaoexp()
        elif resp == 3:
            print('\nMatrizes\n')
            matrix()
        elif resp == 4:
            print('Thau Thau')
        elif resp > 5:
            print('\nDigite um numero valido')
            return menu()

    except:
        print('Algo deu errado tente novamente\n')
        return menu()






def funcoes():
    print(
          '\n1. Calcular Raizes '
          '\n2. Calcular funcao em x pedido '
          '\n3. Calcular Vertice '
          '\n4. Gerar grafico '
          '\n5. Voltar ao menu ')
    try:
        resp = int(input('\nQual desses voce deseja calcular? '))
        if resp == 1:
            a = int(input('\nDigite o A da Funcao: '))
            b = int(input('Digite o B da Funcao: '))
            c = int(input('Digite o C da Funcao: '))
            delta = b ** 2 - 4 * a * c
            if delta <= -1:
                delta *= -1
                delta = math.sqrt(delta)
                bb = -b / (2 * a)
                delta = delta / (2 * a)
                raiz = str(delta) + 'i'
                print('\nA raiz x1 = {} + {}'.format(bb, raiz))
                print('A raiz x1 = {} - {}'.format(bb, raiz))
                funcoes()
            elif delta > 0:
                bask1 = (-b + math.sqrt(delta)) / 2 * a
                bask2 = (-b - math.sqrt(delta)) / 2 * a
                print('As raizes da equacao sao: x1 = {:.2f} e x2 = {:.2f}'.format(bask1, bask2))
                funcoes()
            elif delta == 0:
                bask1 = (-b + math.sqrt(delta)) / 2 * a
                print('A unica raiz da equacao e {} '.format(bask1))
                funcoes()
        elif resp == 2:
            a = int(input('\nDigite o valor de A: '))
            b = int(input('Digite o valor de B: '))
            x = int(input('Digite o valor de X: '))
            resolucao = a * x + b
            print('\nf({}) = {}'.format(x, resolucao))
            funcoes()
        elif resp == 3:
            a = int(input('\nDigite o valor de A:'))
            b = int(input('Digite o valor de B:'))
            c = int(input('Digite o valor de C:'))
            delta = b ** 2 - 4 * a * c
            xv = -b / (2 * a)
            yv = -delta / (4 * a)
            if a > 0:
                print('\nA equacao possui um ponto de maximo')
                print('O Xv = {} e o Yv = {}\n'.format(xv, yv))
                funcoes()
            elif a < 0:
                print('\nA equacao possui um ponto de minimo')
                print('O Xv = {} e o Yv = {}\n'.format(xv, yv))
                funcoes()
            elif a == 0:
                print('\nNao foi possivel fazer os vertices, tente novamente ')
                funcoes()

        elif resp == 4:
            a = int(input('\nDigite o valor de A:'))
            b = int(input('Digite o valor de B:'))
            c = int(input('Digite o valor de C:'))
            delta = b ** 2 - 4 * a * c
            bask1 = (-b + math.sqrt(delta)) / 2 * a
            bask2 = (-b - math.sqrt(delta)) / 2 * a
            if delta < 0:
                print('Impossivel de fazer grafico')
                return funcoes()
            else:
                plt.plot(bask1,bask2)
                plt.show()

        elif resp > 5:
            print('Digite um valor valido')
            return funcoes()
        elif resp == 5:
            print('Voltando ao menu')
            return menu()
    except:
        print('\nAlgo deu errado tente novamente')
        return funcoes()




def funcaoexp():
    try:
        print('\n1. Verificar se é crescente ou decrescente'
            '\n2. Calcular funcao em x pedido'
            '\n3. Gerar grafico'
            '\n4. Voltar ao menu')
        resp = int(input('\nO que voce deseja calcular? '))
        if resp > 4:
            print('Digite uma opcao valida')
            return funcaoexp()
        if resp == 1:
            print('\n𝒇(𝒙)=𝒂𝒃**x')
            a = int(input('\nDigite o valor de A: '))
            b = int(input('Digite o valor de B: '))
            if a >=1:
                print('\nA funcao e crescente')
                return funcaoexp()
            elif a<1:
                print('\nA funcao e decrescente')
                return funcaoexp()

        if resp == 2:
            print('\n𝒇(𝒙)=𝒂𝒃**x')
            a = int(input('\nDigite o valor de A: '))
            b = int(input('Digite o valor de B: '))
            x = int(input('Digite o valor de X: '))
            print('O resultado da equacao e: {}'.format((a*b)**x))
            return funcaoexp()
        if resp == 3:
            a = int(input('\nDigite o valor de A: '))
            b = int(input('Digite o valor de B: '))
            x = int(input('Digite o valor de X: '))
            y = (a*b)**x
            plt.subplots(1)
            plt.plot(1,y)
            plt.show()
            return funcaoexp()
        if resp == 4:
            print('Voltando ao menu')
            return menu()
    except:
        print('\nAlgo deu errado tente novamente')
        return funcaoexp()



def matrix():
    lin = int(input('Número de linhas da matriz: '))
    col = int(input('Número de colunas da matriz: '))
    matriz = gerar_matriz(lin, col)

    printar_matriz(matriz)

    while True:
        print('\n1. Determinante (2x2 ou 3x3)',
              '\n2. Multiplicação',
              '\n3. Matriz transposta')
        opcao = input('\nQual opcao vc deseja escolher ')
        if opcao == '1':
            determinante(matriz)
        elif opcao == '2':
            multiplicar(matriz)
        elif opcao == '3':
            transposta(matriz)
        elif opcao == '':
            break


def determinante(matriz):
    lin = len(matriz)
    col = len(matriz[0])

    if lin != col:
        print('Matriz não é quadrada...')
        return None

    ordem = lin

    if ordem == 1:
        return matriz[0][0]
    elif ordem == 2:
        return (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
    elif ordem == 3:
        det = 0

        # regra de sarrus
        sarrus = matriz
        for l in range(lin):
            sarrus[l].append(matriz[l][0])
            sarrus[l].append(matriz[l][1])

        # somas e subtrações
        for i in range(ordem):
            det += sarrus[0][i] * sarrus[1][i+1] * sarrus[2][i+2]
        for i in range(2, 5):
            det -= sarrus[0][i] * sarrus[1][i-1] * sarrus[2][i-2]

        return det

def multiplicar(matriz):
    lin1 = len(matriz)
    col1 = len(matriz[0])
    lin2 = int(input('Número de linhas da segunda matriz: '))
    col2 = int(input('Número de colunas da segunda matriz: '))

    if col1 == lin2:
        print('A multiplicação é possivel!\n')
        matriz2 = gerar_matriz(lin2, col2)

        A = np.array(matriz)
        B = np.array(matriz2)

        result = np.matmul(A, B)

        printar_matriz(result)
    else:
       print('Multiplicação não é possivel...')

def transposta(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    transp = []

    # transpõe matriz
    for c in range(col):
        linha = []
        for l in range(lin):
            linha.append(matriz[l][c])
        transp.append(linha)

    printar_matriz(transp)

def printar_matriz(matriz):
    lin = len(matriz)
    col = len(matriz[0])

    for l in range(lin):
        linha = ''
        for n in range(col):
            linha += '[' + str(matriz[l][n]) + ']'
        print(linha)

def gerar_matriz(linhas, colunas):
    matriz = []

    for l in range(linhas):
        linha = []
        for c in range(colunas):
            valor = int(input('Valor do elemento [' + str(l + 1) + '][' + str(c + 1) + '] da matriz: '))
            linha.append(valor)
        matriz.append(linha)

    return matriz
menu()