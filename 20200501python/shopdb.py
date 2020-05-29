import sqlite3
#conn = sqlite3.connect('myshop.db')

def create_table(conn):
    c = conn.cursor()
    sql = """
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        desc TEXT NOT NULL,
        image TEXT NOT NULL
    )
"""
    c.execute(sql)

    conn.commit()
    conn.close()

def insert_product(conn, name, price, desc, img):
    c = conn.cursor()
    sql = """
        INSERT INTO products (name, price, desc, image)
        VALUES( ?, ?, ?, ?)
    """
    c.execute(sql, (name, price, desc, img))
    conn.commit()

#insert_product(conn, 'card', 55, 'This is a card', 'https://ctl.s6img.com/society6/img/YQHZoPA8swK9p3a6cTzU9AwPfEI/w_1500/cards/alternate/~artwork,fw_1300,fh_2000,fx_-495,fy_-130,iw_2280,ih_2280/s6-original-art-uploads/society6/uploads/misc/9dadec635d104cd29ce8446bd78bca2e/~~/pink-puff-aesthetic-cards.jpg')

def select_products(conn):
    c = conn.cursor()
    sql = "SELECT id, name, price, desc, image FROM products"
    c.execute(sql)
    return c.fetchall()

#print(select_products(conn))

def select_by_id(conn, sid):
    c = conn.cursor()
    sql = "SELECT id, name, price, desc, image FROM products WHERE id = " + str(sid)
    c.execute(sql)
    return c.fetchone()

#print(select_by_id(conn, 1))

def update_product(conn, id, name, price, desc, image):
    sql = """
        UPDATE products
        SET name = ?,
            price = ?,
            qty = ?
        WHERE id = ?
    """
    c = conn.cursor()
    c.execute(sql, (price, name, desc, image, id))
    conn.commit()