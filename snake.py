# creating snake class as child class of reptile

from reptile import Reptile
class snake(Reptile):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.forked_tongue = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        return "I can smell the taste.....:"

snake_object = snake()
print("This function is from snake class " + snake_object.use_tongue_to_smell())
print("This function is from reptile class " + snake_object.seek_heat())
print("This function is from animal class " + snake_object.eat())
