# sameName2.py

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
