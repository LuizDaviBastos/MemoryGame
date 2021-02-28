import random as Aleatorio

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
posicoesGlobais = []
globalMatrizOculta = [
    ["*", "*", "*", "*"],
    ["*", "*", "*", "*"],
    ["*", "*", "*", "*"],
    ["*", "*", "*", "*"]
]
matriz = []
matrizOcultaStr: str
jogadas = 0


def obterMatrizAleatoria():
    # retorna uma matriz 4x4, contendo 8 pares de numeros (de 1 a 8)
    matrizPrincipal = [[], [], [], []]
    posicao = 0
    for indice in range(4):
        posicao = obterPosicaoUnica()
        if matrizPrincipal[posicao].__len__() <= 0:
            matrizPrincipal[posicao] = Aleatorio.sample(
                (lista1 if indice <= 1 else lista2), 4)
            continue
    return matrizPrincipal


def obterPosicaoUnica():
    global posicoesGlobais
    posicao = 0
    posicoes = [0, 1, 2, 3]
    for p in posicoesGlobais:
        posicoes.remove(p)
    if posicoes.__len__() > 0:
        posicao = Aleatorio.sample(posicoes, 1)[0]
        posicoesGlobais.append(posicao)
    return posicao


def configurarMatrizOculta(linhaColuna: [] = [], value=0):
    matrizStr = ""
    if linhaColuna.__len__() > 0:
        linhaColuna = linhaColuna.replace("[", "").replace("]", "").split(",")
        globalMatrizOculta[int(linhaColuna[0])][int(linhaColuna[1])] = value

    for indice in range(4):
        for subIndice in range(4):
            matrizStr += F"{globalMatrizOculta[indice][subIndice]} "
        matrizStr += "\n"
    return matrizStr


def obterValorMatriz(posicao: [], matriz):
    posicao = posicao.replace("[", "").replace("]", "").split(",")
    return matriz[int(posicao[0])][int(posicao[1])]


def eValido(posicao):
    global globalMatrizOculta
    posicao = posicao.replace("[", "").replace("]", "").split(",")
    valido = False

    if (type(posicao) is list and posicao.__len__() == 2 and int(posicao[0]) <= 3 and int(posicao[1]) <= 3):
        valor = globalMatrizOculta[int(posicao[0])][int(posicao[1])]
        if (type(valor) is not int and valor.replace(" ", "") == "*"):
            valido = ""
        else:
            valido = "Posição já escolhida."
    else:
        valido = "Posição inválida."
    return valido


def rodada():
    primeiroValor = 0
    segundoValor = 0

    def primeiraJogada():
        global jogadas
        global matrizOcultaStr
        if jogadas <= 0:
            matrizOcultaStr = configurarMatrizOculta()

        print(matrizOcultaStr)
        posicao = input("Escolha a primeira posição\n")
        valido = eValido(posicao)
        while valido != "":
            print(valido)
            posicao = input("Escolha a primeira posição\n")
            valido = eValido(posicao)
        valor = obterValorMatriz(posicao, matriz)
        matrizOcultaStr = configurarMatrizOculta(posicao, valor)
        print(matrizOcultaStr)
        return valor

    def segundaJogada():
        global matrizOcultaStr
        posicao = input("Escolha a segunda posição\n")
        valido = eValido(posicao)
        while valido != "":
            print(valido)
            posicao = input("Escolha a segunda posição\n")
            valido = eValido(posicao)
        valor = obterValorMatriz(posicao, matriz)
        matrizOcultaStr = configurarMatrizOculta(posicao, valor)
        print(matrizOcultaStr)
        return valor

    primeiroValor = primeiraJogada()
    segundoValor = segundaJogada()
    global jogadas
    jogadas = jogadas + 1
    return (primeiroValor == segundoValor)


def reinciarMatrizOculta():
    global globalMatrizOculta
    global matrizOcultaStr
    matrizString = ""
    for index in range(4):
        for subIndex in range(4):
            globalMatrizOculta[index][subIndex] = "*"
            matrizString += F"* "
        matrizString += "\n"
    matrizOcultaStr = matrizString


def ganhou():
    ganhou = True
    global globalMatrizOculta
    for linha in globalMatrizOculta:
        for coluna in linha:
            if type(coluna) is not int and coluna.replace(" ", "") == "*":
                ganhou = False
                break
    return ganhou


def jogo():
    global globalMatrizOculta
    global jogadas
    while not ganhou():
        acertou = rodada()
        if acertou:
            print("Parabens! você acertou")
        else:
            print("Você errou... tente de novo.")
            reinciarMatrizOculta()

        print(globalMatrizOculta)

    if ganhou():
        print("Você conseguiu descobrir todos os pares. Parabéns!")
        print(f"Número de jogadas: {jogadas}")


matriz = obterMatrizAleatoria()
jogo()
