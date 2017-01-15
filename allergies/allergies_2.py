allergens = ['cats','pollen','chocolate','tomatoes','strawberries','shellfish','peanuts','eggs']

class Allergies(object):
    def __init__(self,score):
        binary = [0,0,0,0,0,0,0,0]
        list_of_allergies = []

        score = score % 256
        if score == 0:
            self.lst = []
        elif score == 1:
            self.lst = ['eggs']
        else:
            for i in range(7,-1,-1):
                if (score % 2 == 0 and score != 0):
                    binary[i] = 1
                score= score//2
            for i in range(0,len(binary)):
                if binary[i] == 1:
                    list_of_allergies.append(allergens[i])
    
            self.lst = list_of_allergies

    def is_allergic_to(self,string):
        if string in self.lst:
            return True
        else:
            return False
