#Login Attempts


class User:
    """A class to represent a user profile."""

    def __init__(self, first_name, last_name, age, email, location):
        """Initialize user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # Default value

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name.title()}! Welcome back.")

    def increment_login_attempts(self):
        """Increment login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


user = User("alice", "smith", 25, "alice@email.com", "New York")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")  # Should be 3

user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")  # Should be 0
