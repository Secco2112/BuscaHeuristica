from GraphMap import GraphMap

if __name__ == '__main__':
    graphMap = GraphMap()
    graphMap.generateRandomMap().setHunterAtMiddle().generateRandomGhosts().setHunterRadius()
    graphMap.printMap()
