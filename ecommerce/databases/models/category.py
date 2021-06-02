from ecommerce.databases.models import Model


class Category(Model):
    def __init__(self):
        super(Category, self).__init__('Product_Category')

        # self.logPath = 'ecommerce/logs/customer'