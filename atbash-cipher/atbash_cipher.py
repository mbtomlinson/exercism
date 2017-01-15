import string

def decode(message):
    alphabet = string.ascii_lowercase
    message = message.replace(' ','')
    decoded_message = ''
    for alpha in message:
        decoded_message += alphabet[25 - alphabet.index(alpha)]
    return decoded_message


def encode(message):
    alphabet = string.ascii_lowercase
    message = message.lower()
    message = ''.join(alpha for alpha in message if alpha in alphabet+string.digits)
    encoded_message = ''
    for alpha in message:
        if alpha in string.digits:
            encoded_message += alpha
        else:
            encoded_message += alphabet[25 - alphabet.index(alpha)]
    encoded_message = ' '.join([encoded_message[i:i+5] for i in range(0,len(encoded_message),5)])
    return encoded_message
