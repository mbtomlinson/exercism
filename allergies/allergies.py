allergens = ['cats','pollen','chocolate','tomatoes','strawberries','shellfish','peanuts','eggs']


class Allergies(object):
    def __init__(self,score):
        binary = [0,0,0,0,0,0,0,0]
        list_of_allergies = []

        score = score % 256
        for i in range(7,-1,-1):
           if score >= 2**i:
               binary[7-i] = 1
               score -= 2**i
               
        for i in range(0,len(binary)):
            if binary[i] == 1:
                list_of_allergies.append(allergens[i])
    
        self.lst = list_of_allergies

    def is_allergic_to(self,string):
        if string in self.lst:
            return True
        else:
            return False
    
