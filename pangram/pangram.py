#Script that determines if a string is a pangram.

import unicodedata, string, re

def is_pangram(chars):
    chars = str(unicodedata.normalize('NFD', chars).encode('ascii','ignore'))
    chars = re.sub('\W+','', chars)
    chars = re.sub('_','', chars)
    chars = re.sub('\d','',chars)
    
    chars = set(list(chars.lower()))
    alphabet = set(list(string.ascii_lowercase))
    if chars == alphabet:     
        return True
    else:
        print(chars)
        return False
    
        
