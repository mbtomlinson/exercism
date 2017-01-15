

def sum_of_multiples(z, factors):
    mults = []
    for factor in factors:
        if factor == 0:
            continue
        else:
            for i in range(1,1+(z-1)//factor):
                mults.append(factor*i)
    mults = list(set(mults))
    return sum(mults)
