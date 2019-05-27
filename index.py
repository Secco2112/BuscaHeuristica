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
            print("Fantasma encontrado nas coordenadas [x = %d, y = %d]" %(x, y))
            foundedGhosts.append([x, y])

            positions = graphMap.sweepInRadius(x, y)
            if len(positions) > 0:
                for rPos in positions:
                    graphMap.moveTo(rPos[0], rPos[1])
                    print("Fantasma encontrado dentro do raio de [x = %d, y = %d] nas coordenadas [x = %d, y = %d]" %(x, y, rPos[0], rPos[1]))
                    foundedGhosts.append([rPos[0], rPos[1]])
        elif len(graphMap.sweepInRadius(x, y)) > 0:
            positions = graphMap.sweepInRadius(x, y)
            for rPos in positions:
                graphMap.moveTo(rPos[0], rPos[1])
                print("Fantasma encontrado dentro do raio de [x = %d, y = %d] nas coordenadas [x = %d, y = %d]" % (x, y, rPos[0], rPos[1]))
                foundedGhosts.append([rPos[0], rPos[1]])

    graphMap.printMap()
