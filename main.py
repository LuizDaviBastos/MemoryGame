import random as Random


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
globalPositions = []
globalMatrizHidden = [
    ["*", "*", "*", "*"],
    ["*", "*", "*", "*"],
    ["*", "*", "*", "*"],
    ["*", "*", "*", "*"]
]


def getMatriz(matriz: list = []):
    mainMatriz = [[], [], [], []]
    position = 0
    for index in range(4):
        position = getPosition()
        if mainMatriz[position].__len__() <= 0:
            mainMatriz[position] = Random.sample(
                (list1 if index <= 1 else list2), 4)
            continue
    return mainMatriz


def getPosition():
    position = 0
    positions = [0, 1, 2, 3]
    for p in globalPositions:
        positions.remove(p)
    if positions.__len__() > 0:
        position = Random.sample(positions, 1)[0]
        globalPositions.append(position)
    return position


def showMatriz():
    matrizString = ""
    for row in mainMatriz:
        for column in row:
            breaking = ("\n" if row.index(column) >= 3 else "")
            matrizString += f"{column} {breaking}"
    print(matrizString)
    pass

def setValueInHidden(rowColumn: [], value):
    matrizString = ""
    matrizHidden = globalMatrizHidden
    matrizHidden[rowColumn[0]][rowColumn[1]] = value

    for index in range(4):
        for subIndex in range(4):
            matrizString += F"{matrizHidden[index][subIndex]} "
        matrizString += "\n"
        
    print(matrizString)
    pass

mainMatriz = getMatriz()
#showMatriz()
setValueInHidden([0,1], 3)