class StudentData:
    # @staticmethod is a python decorator
    # and when you are making class method static
    # you don't to use self and as well as you can directly access
    # member by class name
    @staticmethod
    def print_message_student():
        return "This message for you!!"
