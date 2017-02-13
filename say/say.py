def say(number):
    if  type(number) is not int:
        raise AttributeError('Input must be an integer')
    num_string = str(number)
    digits = len(num_string)
    thousands = digits // 3
    num_list = []
    if (digits%3!=0):
        num_list.append(num_string[0:digits%3])
    for i in range(thousands):
        num_list.append(num_string[(digits%3)+(3*i):(digits%3)+(3*i)+3])
    output = ''
    ones = {
               '1':'one',
               '2': 'two',
               '3': 'three',
               '4': 'four',
               '5': 'five',
               '6': 'six',
               '7': 'seven',
               '8': 'eight',
               '9': 'nine',
               }
    
    ten_teens = {'10':'ten',
                       '11': 'eleven',
                       '12': 'twelve',
                       '13': 'thirteen',
                       '14': 'fourteen',
                       '15': 'fifteen',
                       '16': 'sixteen',
                       '17': 'seventeen',
                       '18': 'eighteen',
                       '19': 'nineteen',
                       }
    
    tens = {'2': 'twenty',
            '3': 'thirty',
            '4': 'forty',
            '5': 'fifty',
            '6': 'sixty',
            '7': 'seventy',
            '8': 'eighty',
            '9': 'ninety',
            }
    #Apply the below logic to elements of the num_list to create a list of
    #outputs sans their 'magnitude'
    #TODO: eliminate leading zeroes from elements of num_list
        digits = len(num_string)
        if digits == 1:
            output = ones[num_string]
        elif digits == 2:
            if num_string[0] == '1':
                output = ten_teens[num_string]
            else:
                output = tens[num_string[0]] + '-' + ones[num_string[1]]
        return output


