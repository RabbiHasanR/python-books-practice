class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, country):
        """Initialize first_name, last_name, age and country attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        """Increment login attempts by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login attempts 0"""
        self.login_attempts = 0
    
    def formatted_name(self):
        """Return formatted name"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
    
    def describe_user(self):
        """Prints summary of the user information"""
        print(f"Name: {self.formatted_name().title()}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country.title()}")
    
    def greet_user(self):
        """Print personalized greeting for the user."""
        print(f"Hello, {self.formatted_name().title()}")

# rabbi = User('Rabbi', 'Hasan', 25, 'Bangladesh')
# rabbi.increment_login_attempts()
# rabbi.describe_user()
# print('\n')
# rabbi.greet_user()
# print(f"Login attempts: {rabbi.login_attempts}")
# rabbi.reset_login_attempts()
# print(f"Login attempts: {rabbi.login_attempts}")