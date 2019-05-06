import random
from sty import fg, bg, RgbFg


class GraphMap:

    def __init__(self):
        self.types = []
        self.mapSizeX = 42
        self.mapSizeY = 42
        self.map = [[" "] * self.mapSizeX for _ in range(self.mapSizeY)]
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

        new_value = 0
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

        if return_map:
            return self.map

    def printMap(self):
        fg.set_style('water', RgbFg(0, 119, 190))
        fg.set_style('grass', RgbFg(124, 252, 0))
        fg.set_style('mountain', RgbFg(151, 124, 83))
        print(fg.water)

        for row in self.map:
            for i, cell in enumerate(row):
                if cell == "W":
                    print(fg.water + cell, end="")
                elif cell == "G":
                    print(fg.grass + cell, end="")
                else:
                    print(fg.mountain + cell, end="")
            print("")
