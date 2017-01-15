class Clock(object):
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute
        self.rollover()
        
    def add(self, change):
        self.minute += change
        self.rollover()
        return self

    def rollover(self):
        while self.hour < 0:
            self.hour += 24

        subtract_hour = 0
        while self.minute <0:
            self.minute += 60
            subtract_hour+= -1
        self.hour += int(self.minute/60) + subtract_hour
        self.minute = self.minute % 60
        self.hour = self.hour % 24

    def __str__(self):
         self.rollover()
         return str(self.hour).zfill(2) + ':' + str(self.minute).zfill(2)

    def __eq__(self,other):
         return self.hour == other.hour and self.minute == other.minute
