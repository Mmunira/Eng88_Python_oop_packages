# creating python class

from snake import snake

class Python(snake):
    def __init__(self):

        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "yun yum yum...."

    def climb(self):
        return "up we go....."

    def shed_skin(self):
        return "time to grow out of myself! "

python_object = Python()
print("This climb function is from python class " + python_object.climb())
print("This function is from snake class " + python_object.use_tongue_to_smell()

dog_object = Python()
print(dog_object.eat())

