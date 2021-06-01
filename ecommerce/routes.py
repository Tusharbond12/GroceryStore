from ecommerce import app
from flask import render_template


@app.route('/')
def home():
    return render_template('user/home.html', showCarousel=True)


@app.route('/about-us')
def about():
    return render_template('user/about.html', title='About Us')


@app.route('/contact-us')
def contact():
    return render_template('user/contact.html', title='Contact Us')


@app.route('/login')
def login():
    return render_template('user/auth/login.html', title='Login')


@app.route('/register')
def register():
    return render_template('user/auth/registration.html', title='Registration')


@app.route('/categories/<category>')
def categories(category):
    return render_template('user/categories.html', title=category, showPageBanner=True)


@app.route('/products/<product>')
def products(product):
    return render_template('user/products.html', title=product)


@app.route('/cart')
def cart():
    return render_template('user/cart.html', title='Cart')


@app.route('/checkout')
def checkout():
    return render_template('user/checkout.html', title='Checkout')


@app.route('/search')
def search():
    return render_template('user/search.html', title='Search')