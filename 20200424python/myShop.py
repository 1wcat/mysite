from flask import Flask, render_template
from flask import request, redirect
import sqlite3

import sqlite_test

app = Flask(__name__)

@app.route("/")
def myshop():
    conn = sqlite3.connect('myshop.db')
    pds = sqlite_test.select_products(conn)
    print(pds)

    return render_template("myShop.html", products=pds)