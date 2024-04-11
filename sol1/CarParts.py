class CarParts:
    def __init__(self, wheels, head_light):
        self.__wheels = wheels
        self.__head_light = head_light

    def get_wheels(self):
        return self.__wheels

    def get_head_light(self):
        return self.__head_light

    def new_message(self):
        return "New Car Parts"
