from ecommerce.controllers import Controller
from ecommerce.databases.models.customer import User

class UserController(Controller):
    def __init__(self):
        print('UserController')
        self.user = User()

    def index(self):
        users = self.user.find()
        for user in users:
            print(user)
            return