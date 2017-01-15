import re

def word_count(text):
    text = text.lower()
    text = re.sub('\W+',' ',text)
    text = re.sub('_',' ',text)
    text = text.split()
    count = {}

    for word in text:
        count.setdefault(word, 0)
        count[word] += 1

    return count
