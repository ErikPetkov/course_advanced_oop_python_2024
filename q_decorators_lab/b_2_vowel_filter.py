def vowel_filter(function):

    def wrapper():
        l = function()
        return [el for el in l if el in 'aeouiy']
        # TODO: Implement

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())