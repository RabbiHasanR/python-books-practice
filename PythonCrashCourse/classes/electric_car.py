from car import Car
from battery import Battery

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, range):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery(range)
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car don't need a gas tanks.")

my_tesla = ElectricCar('tesla', 'model s', 2019, 75)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()