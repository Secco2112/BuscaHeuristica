from GraphMap import GraphMap
from GenerateMap import GenerateMap

if __name__ == '__main__':
    gm = GenerateMap()
    gm.setFile("Captura de tela de 2019-05-17 20-19-31.pdf").parseFile()
    exit()

    graphMap = GraphMap()
    graphMap.generateRandomMap().setHunterAtMiddle().generateRandomGhosts().setHunterRadius()
    graphMap.move()
    graphMap.printMap()
