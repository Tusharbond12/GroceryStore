from ecommerce.databases.models import Model


class Order(Model):
    def __init__(self):
        super(Order, self).__init__('Order')
