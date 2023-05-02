from collections import namedtuple
from backpack import BackPack

class Person:
    def __init__(self, name, map_, backpack):
        self.name = name
        self._map = map_

    def __repr__(self):
        return f"Person({self.name!r})"

    def move_left(self):


class Room:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self._message = ''

    @property
    def message(self):
        return """
        You have entered a mystery room filled with dread.
        Do you want to open the box in the corner?"""

    def __repr__(self):
        return f"Room({self.name}, {self.items})"


class Map:
    def __init__(self, size=(5,5)):
        self.x, self.y = size
        self.grid = []
        for i in range(x):
            self.grid.append([])
            for j in range(y):
                self.grid[i].append(None)

    def serialize(self):
        with open('temp-file.txt', 'w') as file:
            for row in self.grid:
                for col in row:
                    file.write(col+'\n')
                    file.tell()

    def update_file(self, x, y):
        with open('temp-file.txt', 'a+') as file:
            file.readlines()[x*self.y + y]

    def get_pos(self, x, y):
        return self.grid[x][y]

    def set_pos(self, x, y, grid_square):
        self.grid[x][y] = grid_square

map = Map()
room = Room("witch room", [])
map.set_pos(2, 3, room)
print(map.grid)
person = Person("Zomby Raf",map)

person._map.set_pos(0, 0, person)

