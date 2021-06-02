from ecommerce.controllers import Controller
from ecommerce.databases.models.category import Category

class CategoryController(Controller):
    def __init__(self):
        self.category = Category()

    def index(self):
        categories = self.category.find()
        for category in categories:
            print(category)
        return categories

    def top_3_categories(self):
        categories = self.category.aggregate([{'$limit': 3}])
        return categories