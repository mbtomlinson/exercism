


def abbreviate(string):
    acronym = ''
    for i in range(0,len(string)):
        if i == 0:
            acronym += string[i]
        else:
            if string[i-1] in [' ', '-'] or (string[i].isupper() and not string[i-1].isupper()):
                acronym += string[i]
    acronym = acronym.upper()
    return acronym    
