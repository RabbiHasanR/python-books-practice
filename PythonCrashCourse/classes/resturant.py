class Resturant:
    """A simple attemt to model a resturant"""

    def __init__(self, resturant_name, cuisine_type):
        """Initalize resturant_name and cuisine_type attributes"""
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def set_number_served(self, number):
        """set number served"""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't set negetive number.")
    
    def increment_number_served(self, increment_number):
        """Increment number_served"""
        self.number_served += increment_number
    
    def read_number_served(self):
        """Read number served"""
        return self.number_served
    
    def describe_resturant(self):
        """print out resturant information"""
        print(f"Resturant name is {self.resturant_name}")
        print(f"Cusine type is {self.cuisine_type}")
    
    def open_resturant(self):
        """Indicating that resturant is open with message"""
        print(f'{self.resturant_name} is open')


# cafee_71 = Resturant('Cafee 71', 'Drinking bar')
# kfc = Resturant('KFC', 'Fast food')
# sultan_dine = Resturant('Sultan dines', 'Various foods')

# cafee_71.describe_resturant()
# cafee_71.set_number_served(10)
# cafee_71.increment_number_served(10)
# print(cafee_71.read_number_served())
# print('\n')
# kfc.describe_resturant()
# kfc.set_number_served(20)
# kfc.increment_number_served(10)
# print(kfc.read_number_served())
# print('\n')
# sultan_dine.describe_resturant()
# sultan_dine.set_number_served(30)
# sultan_dine.increment_number_served(10)
# print(sultan_dine.read_number_served())