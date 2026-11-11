#Battery Upgrade


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=65):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 65:
            range_km = 240
        elif self.battery_size == 100:
            range_km = 380

        print(f"This car can go about {range_km} km on a full charge.")

    def upgrade_battery(self):
        """Upgrade battery to 100 kWh if not already."""
        if self.battery_size != 100:
            self.battery_size = 100
            print("Battery upgraded to 100 kWh!")
        else:
            print("Battery is already at maximum capacity (100 kWh).")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class and electric car specific attributes."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        self.battery.describe_battery()


my_car = ElectricCar("tesla", "model s", 2024)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()

print()

my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()
