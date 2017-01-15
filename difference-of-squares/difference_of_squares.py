def square_of_sum(x):
    sum = 0
    for n in range(1,x+1):
        sum +=n
    return sum**2

def sum_of_squares(y):
    sum = 0
    for n in range(1,y+1):
        sum+=n**2
    return sum

def difference(z):
    return square_of_sum(z) - sum_of_squares(z)
