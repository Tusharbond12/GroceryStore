from ecommerce.databases.models import Model


class Customer(Model):
    def __init__(self):
        super(Customer, self).__init__('Customer')
        self.hidden_fields = ['password']

        # self.logPath = 'ecommerce/logs/customer'