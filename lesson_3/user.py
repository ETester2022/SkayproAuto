class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.lname = last_name  
    
    def say_name(self):
        print(self.name)

    def say_last_name(self):
        print(self.lname)

    def say_name_last_name(self):
        print(self.name, self.lname)

