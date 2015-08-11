#! python3
# This is an example of an error, calling stack or getting the traceback as a string.

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()

