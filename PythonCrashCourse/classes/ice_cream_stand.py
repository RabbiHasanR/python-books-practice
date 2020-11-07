from resturant import Resturant

class IceCreamStand(Resturant):
    """Represent aspects of a resturant, specifict to ice cream stand"""

    def __init__(self, resturant_name, cuisine_type, flavors):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(resturant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Display all flavors"""
        print('All flavors:')
        for flavor in self.flavors:
            print(f"\t{flavor}")

ice_cream_stand = IceCreamStand('vi vi iceream', 'ice cream', ['vanila', 'strawberry'])
ice_cream_stand.describe_resturant()
ice_cream_stand.display_flavors()