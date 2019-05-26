from GraphMap import GraphMap
from GenerateMap import GenerateMap

if __name__ == '__main__':
    foundedGhosts = []

    graphMap = GraphMap()
    graphMap.setMapFile("mapa.txt").getMapFromFile().setHunterAtMiddle().generateRandomGhosts().setHunterRadius()

    if len(foundedGhosts) < graphMap.ghostCount:
        pos = graphMap.getNextPositionToMove()
        x = pos[0]
        y = pos[1]

        if graphMap.foundGhostInPosition(x, y):
            graphMap.moveTo(x, y)

    #graphMap.printMap()
