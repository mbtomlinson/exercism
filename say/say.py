import re

def say(number):
    if i not in list(range(10)).append('e') for i in list(number):
        raise AttributeError('Invalid input')
    output = ''
    ones = {'1':'one',
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
    
    if len(number) == 1:
        output = ones[number]
    elif len(number) == 2:
        if number[0] == '1':
            output = ten_teens[number]
        else:
            output = tens[number[0]] + '-' + ones[number[1]]
    return output

