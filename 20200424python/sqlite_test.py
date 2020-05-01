import sqlite3  
conn = sqlite3.connect('myshop.db')

def create_table(conn):
  c = conn.cursor()
  sql = """
    CREATE TABLE products (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      price REAL NOT NULL,
      qty INTEGER NOT NULL
    )
  """
  c.execute(sql)
  conn.commit()
  #conn.close()

def insert_product(conn, name, price, qty):
  c = conn.cursor()
  sql = """
    INSERT INTO products (name, price, qty)
    VALUES (?, ?, ?)
  """
  #c.execute(sql, ('Pen', 15, 45))
  #c.execute(sql, ('Cup', 80, 5))
  #c.execute(sql, ('Notebook', 25, 20))
  c.execute(sql, (name, price, qty))
  conn.commit()

def select_products(conn):
  c = conn.cursor()
  sql = "SELECT id, name, price, qty FROM products"
  c.execute(sql)
  pds = c.fetchall()
  for pd in pds:
    print('{:10}{:>10}{:10}{:10}'.format(pd[0], pd[1], pd[2], pd[3]))
  return pds

def update_product(conn, id, price, qty):  
    sql = """
        UPDATE products
        SET price = ?,
            qty = ?
        WHERE id = ?
    """
    c = conn.cursor()
    c.execute(sql, (price, qty, id))
    conn.commit()

def delete_product(conn, id):
  sql="""
    DELETE FROM products WHERE id = ?
  """
  c = conn.cursor()
  c.execute(sql, (id,))
  conn.commit()

#create_table(conn)
#insert_product(conn, 'Card', 5, 10)
#insert_product(conn, 'Ruler', 50, 70)
#insert_product(conn, 'Zipper', 30, 30)
#insert_product(conn, 'Eraser', 20, 42)
#update_product(conn, 1, 100, 90)
delete_product(conn, 10)
select_products(conn)

conn.close()