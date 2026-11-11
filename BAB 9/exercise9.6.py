#Ice Cream Stand

class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"Restaurant: {self.restaurant_name} ({self.cuisine_type})")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


class IceCreamStand(Restaurant):
    """A class to represent an ice cream stand, a special kind of restaurant."""

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        """Initialize attributes of the parent class, then ice cream specific attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry",
                        "mint chip", "cookie dough"]

    def display_flavors(self):
        """Display the available ice cream flavors."""
        print(f"\nFlavors available at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"  - {flavor.title()}")


ice_cream_stand = IceCreamStand("Frosty Scoops")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
