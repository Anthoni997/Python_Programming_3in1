#Number Served

class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"Restaurant: {self.restaurant_name} ({self.cuisine_type})")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, additional):
        """Increment the number of customers served."""
        self.number_served += additional


restaurant = Restaurant("The Golden Fork", "Italian")

print(f"Number served: {restaurant.number_served}")

restaurant.number_served = 50
print(f"Number served (after direct change): {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Number served (after set_number_served): {restaurant.number_served}")

restaurant.increment_number_served(75)
print(f"Number served (after increment by 75): {restaurant.number_served}")
