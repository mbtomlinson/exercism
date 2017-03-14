def largest_product(series, digits):
    if digits>len(series):
        raise ValueError
    if not digits>=0 and type(digits)==int:
        raise ValueError

    products=[]
    largest = 0
    num_of_potential_solutions = len(series) + 1 - digits

    for i in range(0,num_of_potential_solutions):
        product = 1
        subset = series[i:i+digits]
        for j in range(0, len(subset)):
            product *= int(subset[j])
        products.append(product)
        
    for product in products:
        if product > largest:
            largest = product
    return largest
