def add(x,y):
    return x + y


def subtract(x,y):
    return x - y


def multiply(x,y):
    return x * y


def divide(x,y):

    if y == 0:
        raise ValueError('can not divide by zero') #keywword used to raise exceptions and stop the control of the programe 
    return x / y


