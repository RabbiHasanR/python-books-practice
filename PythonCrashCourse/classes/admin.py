from user import User
from privileges import Privileges

class Admin(User):
    """Represent aspects of a user, specifict to admin"""

    def __init__(self, first_name, last_name, age, country):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an admin.
        """
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()
    

admin = Admin('Rabbi', 'Hasan', 25, 'Bangladesh')
admin.describe_user()
admin.privileges.show_privileges()