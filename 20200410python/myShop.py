from flask import Flask, render_template

products = {
  "sku01": { "id": "sku01", "name": "Pen", "price": 15, "desc": "This is a pen"},
  "sku02": { "id": "sku02", "name": "Cup", "price": 80, "desc": "This is a cup"},
  "sku03": { "id": "sku03", "name": "Notebook", "price": 25, "desc": "This is a notebook"}
}

cart = {
    "sku01": 2,
    "sku02": 5
}
app = Flask(__name__)

@app.route("/")
def myshop():
    return render_template("myshop.html", products=products, cart=cart)

@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)
