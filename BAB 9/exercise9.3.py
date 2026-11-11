#Users

class User:
    """A class to represent a user profile."""

    def __init__(self, first_name, last_name, age, email, location):
        """Initialize user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"Name     : {self.first_name.title()} {self.last_name.title()}")
        print(f"Age      : {self.age}")
        print(f"Email    : {self.email}")
        print(f"Location : {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()}! Welcome back.")


user_1 = User("alice", "smith", 25, "alice@email.com", "New York")
user_2 = User("bob", "johnson", 30, "bob@email.com", "London")
user_3 = User("charlie", "brown", 22, "charlie@email.com", "Jakarta")

for user in [user_1, user_2, user_3]:
    user.describe_user()
    user.greet_user()
    print()
