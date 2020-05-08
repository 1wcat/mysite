from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

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
      "desc": "Blue notebook",
      "image": "https://dynamic.zacdn.com/hsK4OUIb7biUSH5T528dstP0utg=/fit-in/346x500/filters:quality(95):fill(ffffff)/http://static.hk.zalora.net/p/kikki-k-6161-4339335-1.jpg"
     },
  "sku04": { 
      "id": "sku04", 
      "name": "Stapler", 
      "price": 30, 
      "desc": "great stapler",
      "image": "https://images-na.ssl-images-amazon.com/images/I/61hLan93NbL._AC_SX466_.jpg"
      },
}

mycart = {}

@app.route("/")
def myshop():
    return render_template("myshop.html", products=products)

@app.route("/product/<id>")
def product(id):
    pd = products[id]
    return render_template("product.html", product=pd)

@app.route("/cart")
def cart():
    total = 0
    for id, num in mycart.items():
        pd = products[id]
        total += pd['price'] * num

    return render_template("cart.html", mycart=mycart, product=products, total=total)

@app.route("/add-cart/<id>")
def addCart(id):
    mycart[id] = mycart.get(id, 0) + 1
    return redirect('/cart')

@app.route('/add-product', methods = ['GET', 'POST'])
def addProduct():
  if request.method == 'POST':
    name = request.form.get('name')
    price = request.form.get('price')
    products['sku' + str(len(products))] = { 
      'name': name, 
      'price': price
    }
    return redirect('/')

  return render_template('add-product.html')
 

