class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.lName = last_name  
    
    def sayName(self):
        print(self.name)

    def sayLastName(self):
        print(self.lName)

    def sayNameLname(self):
        print(self.name, self.lName)

