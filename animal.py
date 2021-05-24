# animal file to create Animal class

class Animal:
    pass # when you have to create a class but you dont know what to put it

class Animal:

    def __init__(self): # self refers to the current class
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "keep breathing to stay alive"

    def eat(self):
        return "nom nom nom nom"

    def move(self):
        return "moving all around the world!"

# create an object of our Animal class
# cat = Animal() # creating an object of our Animal class called cat
# print(cat.breathe()) # breathing for cat is abstracted

