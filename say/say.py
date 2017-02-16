def say(number):
    try:
        int(number)
    except ValueError:
        raise AttributeError('Input must be a number')
    number = int(number)
    if number>=1e12:
        raise AttributeError('Input is too large')
    if number<0:
        raise AttributeError('Input must not be negative')
    
    if number == 0:
        return 'zero'
    
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
               '0': '',
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
                       '00': '',
                       }
    
    tens = {'2': 'twenty',
            '3': 'thirty',
            '4': 'forty',
            '5': 'fifty',
            '6': 'sixty',
            '7': 'seventy',
            '8': 'eighty',
            '9': 'ninety',
            '0': '',
            }
    magnitude= {
        1:'',
        2:'thousand',
        3:'million',
        4:'billion',
        }

    num_len = len(num_list)
    
    for element in num_list:
        mag = num_len - num_list.index(element)
        if element == '000':
            continue
        while element[0]=='0':
            element = element[1:]
        edigits=len(element)
        if edigits == 1:
            eoutput = ones[element]
        elif edigits == 2:
            if element[0] == '1':
                eoutput = ten_teens[element]
            elif element[1]!='0':
                eoutput = tens[element[0]] + '-' + ones[element[1]]
            else:
                eoutput = tens[element[0]]
        else:
            if element[1]=='1':
                eoutput = ones[element[0]] + ' hundred and ' + ten_teens[element[1:]]
            elif element[2]!='0':
                eoutput = ones[element[0]] + ' hundred and ' + tens[element[1]] + '-' + ones[element[2]]
            elif element[1]==element[2]=='0':
                eoutput = ones[element[0]] + ' hundred'
            else:
                eoutput = ones[element[0]] + ' hundred and ' + tens[element[1]]

        if edigits==1 and len(num_list)!=1 and mag == 1:
            output+='and '+eoutput
        else:
            output+=eoutput + ' ' + magnitude[mag] + ' '
            
    return output.strip()
