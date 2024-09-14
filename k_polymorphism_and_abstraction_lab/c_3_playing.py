class Guitar:
    def play(self):
        return "Playing the guitar"
class Children:
    def play(self):
        return "Children are playing"

def start_playing(instance):
    return instance.play()

children = Children()
guitar = Guitar()
print(start_playing(children))
print(start_playing(guitar))