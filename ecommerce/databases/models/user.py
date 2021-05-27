from ecommerce.databases.models import Model


class User(Model):
    def __init__(self):
        super(User, self).__init__('users')