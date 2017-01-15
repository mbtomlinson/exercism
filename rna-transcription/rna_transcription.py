def to_rna(string):
    translate = {'G':'C','C':'G','T':'A','A':'U'}
    rna = []
    for i in range(len(string)):
        rna.append(translate[string[i]])
    return ''.join(rna)
