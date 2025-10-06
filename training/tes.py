class Car:
    color= None
    number_of_wheels = None

    def __init__(self, color,number_of_wheels):
        self.color = color
        self.number_of_wheels = number_of_wheels


    def start(self):
        print("The", self.color," broom broom")

car = Car("red",4)
car.start()