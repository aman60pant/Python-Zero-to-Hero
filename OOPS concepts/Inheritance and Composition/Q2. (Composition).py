# Create a class Engine with a method start().
# Create a class Car that has an Engine object as an attribute.
# When Car.start_car() is called, it should internally call Engine.start().

class Engine:
    def start(self):
        print("Engine is starting....")

class Car():
    def __init__(self):
        self.engine = Engine()
    def start_car(self):
        self.engine.start()

car = Car()
car.start_car()