from ecommerce import app
from flask import render_template ,request
from ecommerce.controllers.order_controller import OrderController

from ecommerce.controllers.customer_controller import CustomerController
from ecommerce.controllers.category_controller import CategoryController

@app.route('/')
def home():
    top_3_categories = CategoryController().top_3_categories()
    return render_template('customer/home.html', showCarousel=True, response={'top_3_categories': top_3_categories})


@app.route('/about-us')
def about():
    return render_template('customer/about.html', title='About Us')


@app.route('/contact-us')
def contact():
    return render_template('customer/contact.html', title='Contact Us')


@app.route('/login')
def login():
    return render_template('customer/auth/login.html', title='Login')


@app.route('/register')
def register():
    return render_template('customer/auth/registration.html', title='Registration')


@app.route('/categories/<category>')
def categories(category):
    return render_template('customer/categories.html', title=category, showPageBanner=True)


@app.route('/products/<product>')
def products(product):
    return render_template('customer/products.html', title=product)


@app.route('/cart')
def cart():
    return render_template('customer/cart.html', title='Cart')


@app.route('/checkout')
def checkout():
    """
          It would pass data (Dictionay Format) coming from cart menu to order controller
          to update data in the Order table and Order Items table , data would be of format decided by person
          doing product functionality , just need to un comment  the function
     """
    # OrderController().Update_data(data)
    #Dummy data
    return render_template('customer/checkout.html', title='Checkout' )

@app.route('/billing')
def billing():
    """
          It would pass data (Dictionay Format) coming from cart menu to order controller
          to update data in the Order table and Order Items table , data would be of format decided by person
          doing product functionality , just need to un comment  the function
     """
    # OrderController().Update_data(data)
    #Dummy data
    return render_template('checkout.html', title='Checkout' )

@app.route('/search')
def search():
    return render_template('customer/search.html', title='Search')