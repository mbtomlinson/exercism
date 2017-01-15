#Extremely messy.  Not proud, but ready to move on.

def encode(string):
    encoded_string = ''
    counter = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            counter+=1
        else:
            if counter == 1:
                encoded_string += string[i]
            else:
                encoded_string += str(counter)+string[i]
            counter = 1
    if string[len(string)-1] != string[len(string)-2]:
        encoded_string += string[len(string)-1]
    else:
        encoded_string+= str(counter)+string[len(string)-1]
    return encoded_string


def decode(string):
    decoded_string = ''
    length = len(string)
    i = 0
    while i < length:
        if string[i].isdecimal() == False and string[i].isspace() == False:
            string = string[:i+1] + ' ' + string[i+1:]
            length +=1
            i+=1
        else:
            i+=1
    string = string.strip().split(' ')
    for j in range(len(string)):
        if string[j]=='':
            characters = ' '
        elif string[j].isdecimal():
            characters = int(string[j])* ' '
        elif len(string[j]) == 1:
            characters = string[j]
        else:
            characters = int(string[j][:len(string[j])-1])* string[j][len(string[j])-1]
        decoded_string += characters

    return decoded_string
