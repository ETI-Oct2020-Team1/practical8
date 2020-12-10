Error_over10 = "Input has more than 10 values"

def add(*args):
    if len(args) > 10:
        result = Error_over10
        return result
    result = 0;
    for n in args:
        result = result + n
        return result
    
