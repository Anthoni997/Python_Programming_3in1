#Imported Restaurant

class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine   : {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

# --- Main program ---
restaurant = Restaurant("The Golden Fork", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
