class Privileges:
    """A simple attempt to model a privileges for an admin."""

    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        """Initialize the battery's attributes."""
        self.privileges = privileges
    
    def show_privileges(self):
        """Show all privileges"""
        for privilege in self.privileges:
            print(privilege)
