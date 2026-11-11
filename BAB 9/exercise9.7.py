# Exercise 9-7: Admin

class User:
    """A class to represent a user profile."""

    def __init__(self, first_name, last_name, age, email, location):
        """Initialize user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"Name     : {self.first_name.title()} {self.last_name.title()}")
        print(f"Age      : {self.age}")
        print(f"Email    : {self.email}")
        print(f"Location : {self.location}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name.title()}! Welcome back.")


class Admin(User):
    """A class to represent an admin user, a special type of User."""

    def __init__(self, first_name, last_name, age, email, location):
        """Initialize User attributes, then Admin-specific attributes."""
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can promote user",
            "can view reports",
        ]

    def show_privileges(self):
        """List the administrator's privileges."""
        print(f"\nPrivileges for admin {self.first_name.title()}:")
        for privilege in self.privileges:
            print(f"  - {privilege}")


admin = Admin("diana", "prince", 35, "diana@admin.com", "Athens")
admin.describe_user()
admin.greet_user()
admin.show_privileges()
