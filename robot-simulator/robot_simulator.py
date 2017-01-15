class NORTH(object):
    def __init__(self):
        self
class EAST(object):
    def __init__(self):
        self
class WEST(object):
    def __init__(self):
        self
class SOUTH(object):
    def __init__(self):
        self

cardinal = [NORTH, EAST, SOUTH, WEST]

class Robot(object):

    def __init__(self,bearing = NORTH, x = 0, y = 0):
        self.x = x
        self.y = y
        self.coordinates = (self.x,self.y)
        self.bearing = bearing
    
    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        elif self.bearing == WEST:
            self.x -= 1
        self.coordinates = (self.x,self.y)

    def turn_right(self):
        self.bearing = cardinal[(cardinal.index(self.bearing) + 1)%4]

    def turn_left(self):
        self.bearing = cardinal[(cardinal.index(self.bearing) - 1)%4]

    def simulate(self, directions):
        for direction in list(directions):
            if direction == 'A':
                self.advance()
            elif direction == 'R':
                self.turn_right()
            elif direction == 'L':
                self.turn_left()
