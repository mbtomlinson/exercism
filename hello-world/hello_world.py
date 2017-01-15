#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    print('What is your name?')
    name = input()
    if name == '':
        name = 'World'
    return print('Hello, '+name+'!')

hello()
