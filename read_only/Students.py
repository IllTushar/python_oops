class StudentData:
    def __init__(self, name):
        self.__name = name

    # @property decorator is used to make
    # class member read only , you can't override it
    @property
    def print_name(self):
        return self.__name
