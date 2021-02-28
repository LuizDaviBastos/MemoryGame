import random as Aleatorio


lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
posicoesGlobais = []
globalMatrizHidden = [
    ["*", "*", "*", "*"],
    ["*", "*", "*", "*"],
    ["*", "*", "*", "*"],
    ["*", "*", "*", "*"]
]
matriz = []
matrizOculta: str
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


def configurarMatrizOculta(rowColumn: [] = [], value=0):
    matrizString = ""
    #matrizHidden = globalMatrizHidden

    if rowColumn.__len__() > 0:
        rowColumn = rowColumn.replace("[", "").replace("]", "").split(",")
        globalMatrizHidden[int(rowColumn[0])][int(rowColumn[1])] = value

    for index in range(4):
        for subIndex in range(4):
            matrizString += F"{globalMatrizHidden[index][subIndex]} "
        matrizString += "\n"
    return matrizString


def obterValorMatriz(position: [], matriz):
    position = position.replace("[", "").replace("]", "").split(",")
    return matriz[int(position[0])][int(position[1])]


def isValid(posicao):
    global globalMatrizHidden
    posicao = posicao.replace("[", "").replace("]", "").split(",")
    valido = False

    if (type(posicao) is list and posicao.__len__() == 2 and int(posicao[0]) <= 3 and int(posicao[1]) <= 3):
        value = globalMatrizHidden[int(posicao[0])][int(posicao[1])]
        if (type(value) is not int and value.replace(" ", "") == "*"):
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
        global matrizOculta
        if jogadas <= 0:
            matrizOculta = configurarMatrizOculta()

        print(matrizOculta)
        posicao = input("Escolha a primeira posição\n")
        valido = isValid(posicao)
        while valido != "":
            print(valido)
            posicao = input("Escolha a primeira posição\n")
            valido = isValid(posicao)
        valor = obterValorMatriz(posicao, matriz)
        matrizOculta = configurarMatrizOculta(posicao, valor)
        print(matrizOculta)
        return valor

    def segundaJogada():
        global matrizOculta
        posicao = input("Escolha a segunda posição\n")
        valido = isValid(posicao)
        while valido != "":
            print(valido)
            posicao = input("Escolha a segunda posição\n")
            valido = isValid(posicao)
        valor = obterValorMatriz(posicao, matriz)
        matrizOculta = configurarMatrizOculta(posicao, valor)
        print(matrizOculta)
        return valor

    primeiroValor = primeiraJogada()
    segundoValor = segundaJogada()
    global jogadas
    jogadas = jogadas + 1
    return (primeiroValor == segundoValor)


def reinciarMatrizOculta():
    global globalMatrizHidden
    global matrizOculta
    matrizString = ""
    for index in range(4):
        for subIndex in range(4):
            globalMatrizHidden[index][subIndex] = "*"
            matrizString += F"* "
        matrizString += "\n"
    matrizOculta = matrizString


def ganhou():
    ganhou = True
    global globalMatrizHidden
    for row in globalMatrizHidden:
        for column in row:
            if type(column) is not int and column.replace(" ", "") == "*":
                ganhou = False
                break
    return ganhou


def jogo():
    global globalMatrizHidden
    global jogadas
    while not ganhou():
        acertou = rodada()
        if acertou:
            print("Parabens! você acertou")
        else:
            print("Você errou... tente de novo.")
            reinciarMatrizOculta()

        print(globalMatrizHidden)

    if ganhou():
        print("Você conseguiu descobrir todos os pares. Parabéns!")
        print(f"Número de jogadas: {jogadas}")


matriz = obterMatrizAleatoria()
print(matriz)
jogo()
