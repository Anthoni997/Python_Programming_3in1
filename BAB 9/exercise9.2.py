#Three Restaurants

class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"Restaurant Name : {self.restaurant_name}")
        print(f"Cuisine Type    : {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


restaurant_1 = Restaurant("The Golden Fork", "Italian")
restaurant_2 = Restaurant("Sakura Garden", "Japanese")
restaurant_3 = Restaurant("Spice Route", "Indian")

restaurant_1.describe_restaurant()
print()
restaurant_2.describe_restaurant()
print()
restaurant_3.describe_restaurant()
