from ecommerce.databases.models import Model


class User(Model):
    def __init__(self):
        super(User, self).__init__('Customer')
        self.hidden_fields = ['password']

        # self.logPath = 'ecommerce/logs/user'