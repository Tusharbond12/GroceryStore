from ecommerce.controllers import Controller
from ecommerce.databases.models.customer import Customer

class CustomerController(Controller):
    def __init__(self):
        print('UserController')
        self.customer = Customer()

    def index(self):
        customers = self.customer.find()
        for customer in customers:
            print(customer)
        return customers