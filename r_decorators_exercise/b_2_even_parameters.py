def even_parameters(function):
    def wrapper(*args):
        if any([i for i in args if isinstance(i,str) or i %2 == 1]):
            return "Please use only even numbers!"
        return function(*args)
    return wrapper