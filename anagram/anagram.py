def detect_anagrams(string, list_of_candidates):
    anagrams = []
    letters = sorted(string.lower())
    for candidate in list_of_candidates:
        if string.lower() == candidate.lower():
            continue
        elif letters == sorted(candidate.lower()):
            anagrams.append(candidate)
    return anagrams
