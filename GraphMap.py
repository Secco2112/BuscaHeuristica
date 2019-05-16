import random
from sty import fg, bg, RgbFg


class GraphMap:

    def __init__(self):
        self.types = []
        self.mapSizeX = 42
        self.mapSizeY = 42
        self.map = [[" "] * self.mapSizeX for _ in range(self.mapSizeY)]
        self.original_map = [[" "] * self.mapSizeX for _ in range(self.mapSizeY)]
        self.ghost = {
            "name": "Ghost",
            "symbol": "F",
            "color": (255, 0, 0)
        }
        self.hunterRadius = {
            "name": "Hunter Radius",
            "symbol": "R",
            "color": (255, 70, 0)
        }
        self.radiusSize = 3
        self.radiusPosition = []
        self.ghostCount = 6
        self.hunter = {
            "name": "Hunter",
            "symbol": "H",
            "color": (255, 255, 0)
        }
        self.ghostPositions = []
        self.hunterPosition = []
        self.validDirections = ["up", "down", "left", "right"]
        self.mountTypes()

    def mountTypes(self):
        waterType = {
            "name": "Water",
            "symbol": "W",
            "cost": 12,
            "color": (0, 119, 190)
        }
        grassType = {
            "name": "Grass",
            "symbol": "G",
            "cost": 1,
            "color": (124, 252, 0)
        }
        mountainType = {
            "name": "Mountain",
            "symbol": "M",
            "cost": 70,
            "color": (151, 124, 83)
        }

        self.types.append(waterType)
        self.types.append(grassType)
        self.types.append(mountainType)

    def getTypeBy(self, key, value):
        for type in self.types:
            if type[key] == value:
                return type
        return None

    def getNoiseMap(self):
        noise_map = []

        for y in range(self.mapSizeX):
            new_row = []
            for x in range(self.mapSizeY):
                new_row.append(0)
            noise_map.append(new_row)

        top_of_range = 0
        bottom_of_range = 0
        for y in range(self.mapSizeX):
            for x in range(self.mapSizeY):
                if x == 0 and y == 0:
                    continue
                if y == 0:
                    new_value = noise_map[y][x - 1] + random.randint(-1000, +1000)
                elif x == 0:
                    new_value = noise_map[y - 1][x] + random.randint(-1000, +1000)
                else:
                    minimum = min(noise_map[y][x - 1], noise_map[y - 1][x])
                    maximum = max(noise_map[y][x - 1], noise_map[y - 1][x])
                    average_value = minimum + ((maximum - minimum) / 2.0)
                    new_value = average_value + random.randint(-1000, +1000)
                noise_map[y][x] = new_value

                if new_value < bottom_of_range:
                    bottom_of_range = new_value
                elif new_value > top_of_range:
                    top_of_range = new_value

        difference = float(top_of_range - bottom_of_range)
        for y in range(self.mapSizeX):
            for x in range(self.mapSizeY):
                noise_map[y][x] = (noise_map[y][x] - bottom_of_range) / difference
        return noise_map

    def generateRandomMap(self, return_map=False):
        noise_map = self.getNoiseMap()

        for row in noise_map:
            for i, cell in enumerate(row):
                if cell < 0.3:
                    row[i] = "W"
                elif cell < 0.6:
                    row[i] = "G"
                else:
                    row[i] = "M"

        self.map = noise_map
        self.original_map = noise_map

        if return_map:
            return self.map
        return self

    def setHunterAtMiddle(self):
        x = int(self.mapSizeX / 2)
        y = int(self.mapSizeY / 2)
        self.map[x][y] = self.hunter["symbol"]
        self.hunterPosition = [x, y]
        return self

    def generateRandomGhosts(self):
        ghostPositions = []
        for y in range(self.ghostCount):
            ghostPositions.append([0, 0])

        ghostSymbol = self.ghost["symbol"]

        for i in range(0, self.ghostCount):
            x = random.randint(0, 41)
            y = random.randint(0, 41)
            while self.map[x][y] == ghostSymbol:
                x = random.randint(0, 41)
                y = random.randint(0, 41)
            self.map[x][y] = ghostSymbol
            self.ghostPositions.append([x, y])

        return self

    def isValidPoint(self, x, y):
        return 0 <= x < self.mapSizeX and 0 <= y < self.mapSizeY

    def setHunterRadius(self):
        x = self.hunterPosition[0]
        y = self.hunterPosition[1]
        for i in range(x - self.radiusSize, x + self.radiusSize + 1):
            for j in range(y - self.radiusSize, y + self.radiusSize + 1):
                if self.isValidPoint(i, j):
                    if self.map[i][j] != self.ghost["symbol"] and self.map[i][j] != self.hunter["symbol"]:
                        self.radiusPosition.append([i, j])
                        #self.map[i][j] = self.hunterRadius["symbol"]

    def getNextPositionToMove(self):
        x = -1
        y = -1

        while not self.isValidPoint(x, y):
            randomDirection = self.validDirections[random.randint(0, len(self.validDirections) - 1)]

            if randomDirection == "up":
                x = self.hunterPosition[0] - 1
                y = self.hunterPosition[1]
            elif randomDirection == "right":
                x = self.hunterPosition[0]
                y = self.hunterPosition[1] + 1
            elif randomDirection == "left":
                x = self.hunterPosition[0]
                y = self.hunterPosition[1] - 1
            elif randomDirection == "bottom":
                x = self.hunterPosition[0]
                y = self.hunterPosition[1] + 1

        nextPosition = [x, y]
        return nextPosition

    def move(self):
        next_position = self.getNextPositionToMove()
        current_hunter_position = self.hunterPosition
        self.hunterPosition = next_position

        self.map[current_hunter_position[0]][current_hunter_position[1]] = self.original_map[current_hunter_position[0]][current_hunter_position[1]]
        self.map[next_position[0]][next_position[1]] = self.hunter["symbol"]

    def printMap(self):
        fg.set_style('water', RgbFg(0, 119, 190))
        fg.set_style('grass', RgbFg(124, 252, 0))
        fg.set_style('mountain', RgbFg(151, 124, 83))
        fg.set_style('hunter', RgbFg(255, 255, 0))
        fg.set_style('ghost', RgbFg(255, 0, 0))
        fg.set_style('radius', RgbFg(255, 70, 0))

        for row in self.map:
            for i, cell in enumerate(row):
                if cell == "W":
                    print(fg.water + cell, end=" ")
                elif cell == "G":
                    print(fg.grass + cell, end=" ")
                elif cell == "M":
                    print(fg.mountain + cell, end=" ")
                elif cell == "H":
                    print(fg.hunter + cell, end=" ")
                elif cell == "F":
                    print(fg.ghost + cell, end=" ")
                elif cell == "R":
                    print(fg.radius + cell, end=" ")
            print("")
