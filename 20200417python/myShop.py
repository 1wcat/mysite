from flask import Flask, render_template
from flask import request, redirect

products = {
  "sku01": { 
      "id": "sku01", 
      "name": "Pen", 
      "price": 15, 
      "desc": "This is a pen",
      "image": "https://images-na.ssl-images-amazon.com/images/I/71yM877OpML._AC_SX679_.jpg"
      },
  "sku02": { 
      "id": "sku02", 
      "name": "Cup", 
      "price": 80, 
      "desc": "This is a cup",
      "image": "https://www.ikea.com/my/en/images/products/vaerdera-coffee-cup-and-saucer__0711123_PE727991_S5.JPG"
      },
  "sku03": { 
      "id": "sku03", 
      "name": "Notebook", 
      "price": 25, 
      "desc": "This is a notebook",
      "image": "https://dynamic.zacdn.com/hsK4OUIb7biUSH5T528dstP0utg=/fit-in/346x500/filters:quality(95):fill(ffffff)/http://static.hk.zalora.net/p/kikki-k-6161-4339335-1.jpg"
     },
  "sku04": { 
      "id": "sku04", 
      "name": "Stapler", 
      "price": 30, 
      "desc": "This is a stapler",
      "image": "https://images-na.ssl-images-amazon.com/images/I/61hLan93NbL._AC_SX466_.jpg"
      },
}

cart = {
    "sku01": 2,
    "sku02": 5
}
app = Flask(__name__)

@app.route("/")
def myshop():
    total = 0
    for key in cart:
        qty = cart[key]
        item = products[key]
        total += item['price'] * qty

    return render_template("myShop.html", products=products, cart=cart, total=total)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)

@app.route('/product/<id>/edit', methods = ['GET', 'POST'])
def edit(id):
    prod = products[id]
    if request.method == 'POST':
        prod['name'] = request.form['name']
        prod['price'] = int(request.form['price'])
        prod['desc'] = request.form['desc']
        prod['image'] = request.form['image']
        return redirect('/product/' + id)
    return render_template('product-edit.html', product=prod)

@app.route("/cart/edit", methods = ['GET', 'POST'])
def cartEdit():
    errors = {}
    if request.method == 'POST':
        pen = int(request.form['pen'])
        cup = int(request.form['cup'])
        if pen <= 0:
            errors['sku01'] = 'should be positive'
        if cup <= 0:
            errors['sku02'] = 'should be positive'

        if len(errors):
           return render_template("cart-edit.html", cart=cart, errors=errors) 
        
        cart['sku01'] = pen
        cart['sku02'] = cup
        return redirect('/')
    return render_template("cart-edit.html", cart=cart, errors=errors)