# Class
from CarParts import CarParts


# CarParts inherits by CarDetails class
class CarDetails(CarParts):
    # Constructor.
    def __init__(self, brand, model, wheels, head_light):
        # super keyword refers the parent class members
        super().__init__(wheels, head_light)
        self.brand = brand
        self.model = model

    # When you and add any function in ,
    # your class always use self to access the member variable.

    def print_car(self):
        return f"{self.brand} and {self.model} and no of wheels: {self.get_wheels()} and no of head light {self.get_head_light()}"

    def new_message(self):
        return "New Message"
