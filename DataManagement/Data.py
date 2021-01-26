import sqlite3

# Connect to Database customer.db (does not already exist)

conn = sqlite3.connect('customer.db')

# ------------------ Create a Database Table -----------------

# Create a cursor
c = conn.cursor()

# Create a Table
# c.execute('''CREATE TABLE customers4 (
#             first_name text,
#             last_name text,
#             email text)''')

# Data types: NULL INTEGER REAL TEXT BLOB

# Commit our command
conn.commit()


# ------------------ INSERT ONE RECORD IN A TABLE ---------

c.execute('''INSERT INTO customers VALUES('Emna', 'HNANA', 'emna@gmail.com')
            ''')
print(" Command executed successfully ")

# ------------------ INSERT MANY RECORDS----------------------
many_customers = [('Wes', 'Brown', 'wes@brown.com'), ('Steph', 'Lola', 'steph@lola.com')]

c.executemany('''INSERT INTO customers VALUES 
                    (?, ?, ?)''', many_customers)

conn.commit()

# ------------------- Fetch and Query -------------------------
c.execute("SELECT * FROM customers")
print(c.fetchall())


# Close our connection
conn.close()