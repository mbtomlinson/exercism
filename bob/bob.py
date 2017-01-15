#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    what = what.strip()
    if not what:
        return 'Fine. Be that way!'
    elif what.isspace() == True:
        return 'Fine. Be that way!'
    elif what.isupper() == True:
        return 'Whoa, chill out!'
    elif what.endswith('?')== True:
        return 'Sure.'
    else:
        return 'Whatever.'
