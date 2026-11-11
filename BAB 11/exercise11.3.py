#Employee — Class File

class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize employee attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add a raise to the annual salary. Default raise is $5,000."""
        self.annual_salary += amount
