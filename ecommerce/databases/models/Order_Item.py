from ecommerce.databases.models import Model


class Order_Item(Model):
    def __init__(self):
        super(Order_Item, self).__init__('Order_Item')