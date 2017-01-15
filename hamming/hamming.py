def distance(x,y):
        counter = 0
        for i in range(len(x)):
            if x[i]!=y[i]:
                counter +=1
        return counter
