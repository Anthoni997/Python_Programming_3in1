#Multiple Modules

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
        print(f"Email    : {self.email}")
        print(f"Location : {self.location}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name.title()}! Welcome back.")
        

class Privileges:
    """A class to manage admin privileges."""

    def __init__(self):
        """Initialize default admin privileges."""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can promote user",
            "can view reports",
        ]

    def show_privileges(self):
        """Display all privileges."""
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"  - {privilege}")


class Admin(User):
    """A class to represent an admin user, inheriting from User."""

    def __init__(self, first_name, last_name, age, email, location):
        """Initialize User attributes and compose Privileges."""
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()


admin = Admin("diana", "prince", 35, "diana@admin.com", "Athens")
admin.describe_user()
print()
admin.privileges.show_privileges()
print("\n(In production: User is in user_module.py, Admin+Privileges in admin_module.py)")
