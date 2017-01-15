class NORTH(object):
    def __init__(self):
        self
    def turn_right(self):
        return EAST
    def turn_left(self):
        return WEST
    
class EAST(object):
    def __init__(self):
        self
    def turn_right(self):
        return SOUTH
    def turn_left(self):
        return NORTH
    
class WEST(object):
    def __init__(self):
        self
    def turn_right(self):
        return NORTH
    def turn_left(self):
        return SOUTH
    
class SOUTH(object):
    def __init__(self):
        self
    def turn_right(self):
        return WEST
    def turn_left(self):
        return EAST

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

    def turn_right(self):
        cardinal[cardinal.index(self.bearing) + 1]

    def turn_left(self):
        cardinal[cardinal.index(self.bearing) - 1]

    def simulate(self, directions):
        for direction in list(directions):
            if direction == 'A':
                self.advance()
            elif direction == 'R':
                self.turn_right()
            elif direction == 'L':
                self.turn_left()
