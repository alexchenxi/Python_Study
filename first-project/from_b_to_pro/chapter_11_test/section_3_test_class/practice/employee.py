class Employee:
    """A simple attempt to model an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize employee attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add $5000 to the employee's annual salary."""
        self.annual_salary += amount
