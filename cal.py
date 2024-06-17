

def do_addition(a,b):
    return a+b

def do_sub(a,b):
    return abs(a,b)


def do_dividion(a,b):
    try:
        
        return a/b
    except ZeroDivisionError as e:
        return "cannot be dividd by zero"
